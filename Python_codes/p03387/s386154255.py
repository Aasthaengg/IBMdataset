a=list(map(int,input().split()))
a.sort()
x=(a[2]-a[1])+(a[1]-a[0])//2+((a[1]-a[0])%2)*2
print(x)