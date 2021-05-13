N,M,X,Y = map(int,input().split())

x = list(map(int,input().split()))
y = list(map(int,input().split()))
ans = 'War'
for i in range(-100,101):
    if X < i <= Y and max(x)<i and min(y)>=i:
        ans = 'No War'
        break
print(ans)