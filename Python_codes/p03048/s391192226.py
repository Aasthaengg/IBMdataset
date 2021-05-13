R,G,B,n = map(int, input().split())
ans = 0
for r in range(n//R+1):
    if R*r > n: break
    for g in range(n//G+1):
        ball = R*r + G*g
        if ball > n: break
        if (n-ball)%B==0: ans += 1
print(ans)