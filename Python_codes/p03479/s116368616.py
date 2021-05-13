X,Y = map(int,input().split())

ans = 1
tmp = X

while tmp <= Y:
    tmp = tmp*2
    if tmp <= Y:
        ans+=1

print(ans)