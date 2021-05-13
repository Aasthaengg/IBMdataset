X,Y = map(int,input().split())

ans = 0
tmp = X

while tmp <= Y:
    ans += 1
    tmp = tmp*2
    
print(ans)