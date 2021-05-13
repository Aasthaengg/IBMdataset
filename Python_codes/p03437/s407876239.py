x,y=list(map(int, input().split()))
if x%y:print(x*(y-1))
else:print(-1)