X, Y = map(int,input().split())

A = X
ans = 1

while(1):
    if X*2 > Y:
        break
    X *= 2
    ans += 1

print(ans)