N,Y = input().split()
N = int(N)
Y_k=int(Y)/1000

answer = [-1,-1,-1]
for i in range(N+1):
    for j in range(N+1 - i):
        k = N-i-j
        if 10*i + 5*j + 1*k == Y_k:
            answer = [i,j,k]

print(answer[0],answer[1],answer[2])
