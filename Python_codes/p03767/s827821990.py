## A - AtCoder Group Contest
N = int(input())
A = sorted(map(int, input().split()), reverse=True)
val = 0
for n in range(N):
    val += A[ 2*n + 1 ]
print(val)