n = int(input())
a = list(map(int,input().split()))
a.sort()
a.reverse()
ans = 0
for i in range(1,n*2):
    ans += a[i] if i%2 else 0

print(ans)