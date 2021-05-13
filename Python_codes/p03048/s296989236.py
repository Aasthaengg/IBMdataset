R,G,B,N = map(int, input().split())
ans = 0
for i in range(0,1+N//R):
    #print(i,1 + (N-i*R)//G)
    for j in range(0,1 + (N-i*R)//G):
        k = (N-i*R-j*G)//B
        if N == R*i + G*j + B*k:
            ans += 1

print(ans)