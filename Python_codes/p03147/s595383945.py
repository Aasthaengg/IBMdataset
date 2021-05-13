N = int(input())
h = list(map(int,input().split()))
sw = 0
while max(h) != 0:
    for i in range(N):
        if h[i] == 0:
            continue
        j = 0
        for jj in range(i,N+1):
            if jj == N:
                j = jj
                break
            if h[jj] == 0:
                j = jj
                break
        #print(i,j)
        sw += 1
        for jj in range(i,j):
            h[jj] -= 1
        break
print(sw)