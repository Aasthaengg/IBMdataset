n = int(input())
A = list(map(int,input().split()))

num = {}
ans = 0
for i, v in enumerate(A):
    p = v+i
    m = i-v
    if p not in num:
        num[p] = 1
    else:
        num[p] += 1
    if m in num:
        ans += num[m]
print(ans)