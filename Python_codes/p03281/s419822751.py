from math import sqrt, ceil
n = int(input())
ans = 0
for i in range(1, n+1, 2):
    score = 0
    for d in range(1, ceil(sqrt(i))+1):
        p, m = divmod(i, d)
        if m == 0:
            if p != d:
                score += 2
            else:
                score += 1
    if score == 8:
        ans += 1
print(ans)