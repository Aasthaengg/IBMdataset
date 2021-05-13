a,b=map(int,input().split())
if (a-b)&1:print("IMPOSSIBLE")
else:print(min(a,b)+abs(a-b)//2)