#B - Different Distribution
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
A.sort(key=lambda x: x[1])

print((A[0][0])+A[0][1])