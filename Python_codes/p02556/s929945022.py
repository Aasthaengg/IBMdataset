N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
w,z = [],[]
for x,y in XY:
    w.append(x-y)
    z.append(x+y)

a,b = max(w)-min(w),max(z)-min(z)
print(max(a,b))