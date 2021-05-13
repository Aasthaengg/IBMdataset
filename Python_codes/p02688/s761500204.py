N,K = list(map(int,input().split()))
r = set()
for i in range(K):
  d = int(input())
  r |= set(map(int,input().split()))
print(N-len(r))