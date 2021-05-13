N = int(input())
C = list(map(int, input().strip().split()))
curr = 1000
for i in range(1, N):
    if C[i] > C[i - 1]:
        share, remain = divmod(curr, C[i - 1])
        curr = remain + share * C[i]
print(curr)