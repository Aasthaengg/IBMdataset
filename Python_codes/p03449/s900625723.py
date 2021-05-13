N = int(input())
A =  [list(map(int, input().split())) for _ in range(2)]

max_total = 0
for i in range(N):
    total = sum(A[0][:i+1]) + sum(A[1][i:])
    if max_total < total:
        max_total = total

print(max_total)