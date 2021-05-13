N, M = map(int,input().split())
if N%2 == 1:
    for i in range(1,M+1):
        print(i,N+1-i)
else:
    for i in range(1,M+1):
        if i == N//4+1:
            break
        print(i,N+1-i)
        if i == M:
            quit()
    for j in range(i,M+1):
        print(j+1,N+1-j)