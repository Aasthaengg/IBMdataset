a=list(map(int,input().split()))

a.sort(reverse=True)

s=2*a[0]-a[1]-a[2]

if s%2==0:
    print(s//2)
else:
    s+=1
    print(1+s//2)
