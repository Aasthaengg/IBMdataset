n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)[::-1]
ans = 0
for i in range(2*n):
    if (i+1)%2==0:
        ans += a[i]
print(ans)