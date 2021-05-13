N=int(input())
a=[0,0,0]
for i in range(N):
    a[0],a[1],a[2] = map(int, input().split())
    a.sort()
    if a[0]**2+a[1]**2 == a[2]**2:
        print("YES")
    else:
        print("NO")
