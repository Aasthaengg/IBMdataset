l = []
z = []
w = []
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    l.append([x+y,x,y])
    z.append(x+y)
    w.append(x-y)

l.sort()
z.sort()
w.sort()

ans = max(z[-1]-z[0],w[-1]-w[0])

print(ans)
