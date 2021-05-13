R, G, B, N = map(int, input().split())
ans = 0
Rmax=N//R
Gmax=N//G
for i in range(Rmax+1):
    for j in range(Gmax+1):
        total=i*R+j*G
        if N-total<0:
            break
        elif (N-total)%B==0:
            ans+=1
    if j==0:
        break
print(ans)
