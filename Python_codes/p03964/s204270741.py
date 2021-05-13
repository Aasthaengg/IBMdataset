N = int(input())
T, A = [0]*N, [0]*N

for i in range(N):
    T[i], A[i] = map(int, input().split())
t = a = 1
for i in range(N):
    n = max(-(-t//T[i]), -(-a//A[i]))
    t = n*T[i]
    a = n*A[i]
print(t+a)
