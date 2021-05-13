K = int(input())
N = 50
As = [K//N]*N
K = K%50
for i in range(N):
  if i < N-K:
    As[i] += i
  else:
    As[i] += i+1
print(N)
print(" ".join(map(str, As)))
