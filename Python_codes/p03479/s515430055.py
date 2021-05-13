X,Y = map(int,input().split())
ans = 1
Z = X
while Z <= Y//2:
    Z *= 2
    ans += 1
print(ans)