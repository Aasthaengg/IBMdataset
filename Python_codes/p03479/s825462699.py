X,Y = list(map(int,input().split()))

ans=0
while True:
    if X > Y:
        break
    X=2*X
    ans += 1
print(ans)