n = int(input())
a = list(map(int,input().split()))
INF = 114514191981036436433-4
bl = []

for i in range(n):
    bl.append(a[i] - (i+1))
    
bl.sort()
d = bl[0]
c = [bl[i]-d for i in range(n)]

ans = sum(c)
cur = sum(c)

for i in range(1,n):
    e = c[i] - c[i-1]
    cur = cur + i * e - (n-i) * e
    ans = min(cur,ans)
    
print(ans)