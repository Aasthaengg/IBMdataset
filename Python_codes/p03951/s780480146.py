N = int(input())
s = list(input())
t = list(input())
N2 = N * 2
ans = 0
for i in range(N):
    temp = 0
    ns = s[i:]
    for j, k in zip(ns, t):
        if j == k:
            temp += 1
        else:
            break
    else:
        ans = max(ans, temp)

print(N2 - ans)