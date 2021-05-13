
S = input()
N = len(S)+1
l = [0]
r = [0]

for i in range(N-1):
    if S[i] == '<':
        l.append(l[-1]+1)
    else:
        l.append(0)
    if S[-1-i] == '>':
        r.append(r[-1]+1)
    else:
        r.append(0)

r = r[::-1]
ans = [max(l[i], r[i]) for i in range(N)]
print(sum(ans))