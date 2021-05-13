N = int(input())
A = list(map(int, input().split()))

sm = 0.0
for i in range(N):
    sm += 1/A[i]

print(1/sm)
