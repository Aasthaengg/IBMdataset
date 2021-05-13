n = int(input())

t = []
for i in range(n):
   x,l = map(int,input().split())
   t.append((x+l,x-l))
t.sort()
max_r = -float('inf')
ans = 0
for i in range(n):
    if max_r<=t[i][1]:
        ans+=1
        max_r=t[i][0]
print(ans)