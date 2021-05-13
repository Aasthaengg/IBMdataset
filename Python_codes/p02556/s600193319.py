N = int(input())
lis = []
d1 = []
d2 = []
for i in range(N):
    x,y = map(int,input().split())
    lis.append([x,y])
    d1.append(x-y)
    d2.append(x+y)
ans = max(d1) - min(d1)
ans = max(ans,max(d2) - min(d2))
print(ans)

