N = int(input())
A = list(map(int,input().split()))
dif1 = []
dif2 = []
A.insert(0,0)
A.append(0)
sum = 0
for i in range(N):
    dif1.append(abs(A[i + 1] - A[i]))
    dif2.append(abs(A[i + 2] - A[i]))
    sum += dif1[i]
dif1.append(abs(A[N+1] - A[N]))
sum += dif1[N]

for i in range(N):
    print(sum - dif1[i] - dif1[i+1] + dif2[i])