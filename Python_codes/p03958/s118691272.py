K, T = map(int, input().split())
A = sorted([int(i) for i in input().split()], reverse=True)

print(max(0, A[0]-sum(A[1:])-1))
