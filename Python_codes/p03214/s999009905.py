N = int(input())
A = list(map(int,input().split()))
ave = sum(A) / N
ave_A = [0]*N
output = 10000007
for i in range(N):
  ave_A[i] = abs(A[i] - ave)
for i in range(N):
  output = min(output, ave_A[i])
print(ave_A.index(output))