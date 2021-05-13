n = int(input())
a = list(map(int,input().split()))

s = 0
for i in a:
    s += i

ans = float('inf')
tmp = 0
for i in range(n-1):
    tmp += a[i]
    ans = min(ans,abs(s-tmp-tmp)) 

print(ans)
