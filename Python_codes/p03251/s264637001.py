n,m,x,y = map(int,input().split())
a = max(list(map(int,input().split())))
b = min(list(map(int,input().split())))
ans = "War"
for i in range(x+1,y):
    if i>a and i<=b:
        ans = "No War"
print(ans)