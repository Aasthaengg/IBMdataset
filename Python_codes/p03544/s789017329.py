W = [2,1]
N=int(input())
for i in range(N):
  K=W[0]+W[1]
  W.append(K)
  W.pop(0)
print(W[0])