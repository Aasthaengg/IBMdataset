from sys import stdin

n,x = map(int,input().split())
m = [int(stdin.readline()) for i in range(n)]
m.sort()
ans = 0
for i in m:
    ans += 1
    x -= i 
ans += x//m[0]
print(ans)