N = int(input())
S = input()
score, ans = 0, 0
for i in S:
    if i is 'I': score += 1
    else: score -= 1
    ans = max(score, ans)
print(ans)
