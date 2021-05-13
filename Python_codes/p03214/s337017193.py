N = int(input())
A = list(map(int, input().split()))

ave = sum(A) / len(A)

for i in range(N):
  A[i] = abs(A[i]-ave)

minA = min(A)

print(A.index(minA))