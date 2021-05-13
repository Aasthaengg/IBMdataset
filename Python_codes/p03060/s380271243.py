N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

diff = 0
for i in range(N):
    if V[i] >= C[i]:
        diff += (V[i] - C[i])
print(diff)