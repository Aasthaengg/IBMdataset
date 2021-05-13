N = int(input())
print(min([sum(map(int,list(str(A))))+sum(map(int,list(str(N-A)))) for A in range(1,N)]))