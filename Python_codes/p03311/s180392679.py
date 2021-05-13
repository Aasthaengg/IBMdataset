n = int(input())
a = list(map(int, input().split()))
B, SUM = [], 0

for i in range(n):
    SUM += a[i]-i-1
    B.append(a[i]-i-1)

Bs = sorted(B)
if n%2 == 1:
    b = Bs[n//2]
else:
    b = (Bs[n//2-1]+Bs[n//2])//2
ans = 0
for i in B:
    ans += abs(i-b)
print(ans)