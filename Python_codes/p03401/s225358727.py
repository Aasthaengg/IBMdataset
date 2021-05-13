N = int(input())
A = [0] + list(map(int, input().split()))
diff = []
for i in range(N):
  diff.append(abs(A[i]-A[i+1]))

diff.append(abs(A[-1]))

A += [0]
s = sum(diff)
for i in range(N):
  v = s - diff[i] - diff[i+1]
  v += abs(A[i] - A[i+2])
  print(v)