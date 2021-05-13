N = int(input())
A = [list(map(int, input().split())) for i in range(2)]
print(max([sum(A[0][:i+1])+sum(A[1][i:]) for i in range(N)]))
