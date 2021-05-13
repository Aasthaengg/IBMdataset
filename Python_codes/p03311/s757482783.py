n = int(input())
a = list(map(int,input().split()))

b = []
for i in range(n):
    b.append(a[i]-i-1)
b = sorted(b)

ans = 0
k = b[n//2]
for i in range(n):
    ans += abs(b[i]-k)
print(ans)