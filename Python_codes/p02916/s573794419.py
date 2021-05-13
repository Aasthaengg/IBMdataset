n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
rout = []
for i in range(n):
    ans += b[a[i]-1]
    rout.append(a[i]-1)

for i in range(n-1):
    if rout[i] + 1 == rout[i+1]:
        ans += c[rout[i]]
print(ans)