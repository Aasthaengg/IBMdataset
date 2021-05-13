N,M,K = [int(i) for i in input().split()]

for i in range(0,N+1):
    for j in range(0,M+1):
        ans = i*M+j*N-i*j*2
        if ans==K:
            print("Yes")
            exit()

print("No")