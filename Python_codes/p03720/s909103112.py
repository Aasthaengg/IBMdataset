N, M = map(int,input().split())
a = 0
b = 0
A = []
B = []
city = [0]*N
for i in range(M):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
for i in range(M):
    city[A[i] - 1] += 1
    city[B[i] - 1] += 1
for i in range(N):
    print(city[i])
