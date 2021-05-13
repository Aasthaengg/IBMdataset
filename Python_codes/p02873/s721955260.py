def compute_score(sub):
    max_i = max(sub)
    min_i = min(sub)
    score = max_i * (max_i + 1) * (1 /2) + min_i * (min_i - 1) * (1/2)
    return score

S = input()
sub = [0, 0]
ans = 0
flag = False
for s in S:
    if s == '<' and flag:
        ans += compute_score(sub)
        sub = [0, 0]
        flag = False
    if s == '>':
        flag = True
    if s == '<':
        sub[0] += 1
    else:
        sub[1] += 1
ans += compute_score(sub)
print(int(ans))