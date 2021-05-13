a,b = map(int,input().split())
ans = [(a+b)//2,"IMPOSSIBLE"]
print(ans[(a+b)%2])
