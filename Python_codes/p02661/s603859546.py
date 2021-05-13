n=int(input())
a,b=[],[]
for _ in range(n):
    a_,b_=map(int,input().split())
    a.append(a_)
    b.append(b_)
a.sort()
b.sort()
if n%2:
    print(b[n//2]-a[n//2]+1)
else:
    lower=(a[n//2]+a[n//2-1])/2
    upper=(b[n//2]+b[n//2-1])/2
    print(int(upper*2-(lower*2-1)))