R,G,B,N = map(int,input().split())

ans = 0

for r in range(1+N//R):
    for g in range(1+N//G):
        #print(N-(r*R+g*G),r*R, g*G)
        if N-(r*R+g*G) < 0:
            break
        if (N-(r*R+g*G))%B==0:
            ans += 1
print(ans)