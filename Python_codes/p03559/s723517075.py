N = int(input())
A = sorted(map(int,input().split(" ")))
B = sorted(map(int,input().split(" ")))
C = sorted(map(int,input().split(" ")))

o = []
p = []

i = 0
k = 0
for j in range(N):
    while i < N and A[i] < B[j]:
        i = i + 1
    o.append(i)

    while k < N and B[j] >= C[k]:
        k = k + 1
    p.append(N-k)

sum = 0
for x in range(N):
    sum = sum + o[x] * p[x]

print(sum)