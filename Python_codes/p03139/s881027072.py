n,a,b=map(int,input().split())
if a+b<n:
    Max=min(a,b)
    Min=0
else:
    Max=min(a,b)
    Min=max(a,b)-(n-min(a,b))

print("{0} {1}".format(Max,Min))