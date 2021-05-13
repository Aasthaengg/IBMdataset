N = int(input())
num = {}
for i in range(N):
    A = int(input())
    if A in num.keys():
        num[A] += 1
    else:
        num[A] = 1
ans = 0
for i, j in num.items():
    if j%2 == 1:
        ans += 1
print(ans)
