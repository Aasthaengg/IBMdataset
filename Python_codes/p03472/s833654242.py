import math

n,h = map(int,input().split())
s = []
max_a = 0
for i in range(n):
    a,b = map(int,input().split())
    max_a = max(a,max_a)
    s.append((b,a))

if max_a >= h:
    print(1)
    exit()

s.sort(reverse=True)
ans = 10**9
i = 0
while h > 0 and i < n:
    h -= s[i][0]
    c = max(0,math.ceil(h/max_a))
    ans = min(i+c+1,ans)
    i += 1

print(ans)