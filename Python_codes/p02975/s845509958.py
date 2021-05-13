n=int(input())
a=list(map(int,input().split()))
a.sort()
if sum(a)==0:
    print('Yes')
    exit()
x=[0]*3
x[0] = a.count(a[0])
x[1] = a.count(a[n//2])
x[2] = a.count(a[-1])
x.sort()

if a[0]^a[n//2] == a[-1] and x[0] == x[1] == x[2] == n//3:
    print('Yes')
elif a[0] == 0 and x[0] == n//3 and x[1] == x[2] == n*2//3:
    print('Yes')
else:
    print('No')