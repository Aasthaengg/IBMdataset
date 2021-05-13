import statistics
N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
  B.append(A[i]-(i+1))
#print(B)
b = statistics.median(B)

s = 0
for i in range(N):
  s += abs(A[i] - (b+i+1))
print(int(s))
