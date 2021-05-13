N,K=map(int, input().split())
if K%2==1:
    print((N//K)**3)
else:
    modKp2 = 0
    for i in range(1, N+1):
        if i%K==K//2:
            modKp2+=1
    print((N//K)**3+modKp2**3)