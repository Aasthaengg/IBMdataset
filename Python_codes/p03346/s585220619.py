N = int(input())
chain = [0 for i in range(N+1)]
for i in range(N):
  a = int(input())
  chain[a] = chain[a-1]+1
print(N-max(chain))