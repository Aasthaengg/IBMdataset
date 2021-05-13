N, M = input().split(' ')
N = int(N)
M = int(M)
K1 = input().split(' ')
Like = [int(K1[i]) for i in range(1, len(K1))]
Like = set(Like)
for i in range(N-1):
  K = input().split(' ')
  K = [int(K[i]) for i in range(1, int(K[0])+1)]
  K = set(K)
  Like &= K
print(len(Like))