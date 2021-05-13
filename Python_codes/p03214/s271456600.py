import statistics
N = int(input())
A = list(map(int,input().split()))
MEAN = statistics.mean(A)
D = [abs(a -MEAN) for a in A]
MIN = 100
MIN_I = 0
for i in range(N):
    if MIN > D[i]:
        MIN = D[i]
        MIN_I = i
print(MIN_I)