n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

print(abs(sum(A[0:n:2]) - sum(A[1:n:2])))