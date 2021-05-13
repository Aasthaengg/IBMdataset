N,K = input().split()
N = int(N)
K = int(K)

h = []
h = input().split()

count = 0
for i in range(N):
  if(int(h[i]) >= K):
    count += 1

print(count)
