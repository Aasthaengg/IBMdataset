H, N = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(N):
    H -= A[i]

print(['No','Yes'][H <= 0])