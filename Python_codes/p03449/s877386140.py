import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split()))  for _ in range(2)]

s = 0

result = [0] * N

for i in range(N):
    result[i] = sum(A[0][0:i+1]) + sum(A[1][i:]) 


print(max(result))
