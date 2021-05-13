n,x,y=list(map(int,input().split()))
if x+y<=n:
    Min=0
    if x<=y:
        Max=x
    else:
        Max=y
else:
    Min=(x+y)-n
    if x<=y:
        Max=x
    else:
        Max=y
print("{} {}".format(Max,Min))
