n,m=map(int,input().split())
if n%3==0 or m%3==0 or (n+m)%3==0:print("Possible")
else:print("Impossible")