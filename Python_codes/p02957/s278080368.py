a,b=map(int,input().split())
print(int(min(a,b)+abs(a-b)/2) if (a-b)%2==0 else "IMPOSSIBLE")