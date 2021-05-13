# input
N, X = map(int, input().split())
M = [
    int(input())
    for n in range(N)
]

# check
X -= sum(M)
cnt = N
min_m = min(M)
cnt += X // min_m

print(cnt)