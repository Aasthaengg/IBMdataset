N = int(input())

H = list(map(int,input().split()))
hn = 0
ansL = [0]*N
ansLn = 0


for p in range(N):
    if hn < H[p]:
        ansLn = p
    
    else:
        ansL[ansLn] += 1

    hn = H[p]

print(max(ansL))


