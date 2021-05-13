#32 C - Otoshidama
N,Y = map(int,input().split())

for i in range(N+1):
    for j in range(N+1-i):
        tot = i*10000 + j*5000 + (N-i-j)*1000
        if tot == Y:
            ans = (i,j,N-i-j)
            break
    else:
        continue
    break
else:
    ans = (-1,-1,-1)
print(*ans)