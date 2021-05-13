N, K=map(int, input().split())
d=[]
A=[]
plus=set()
for i in range(K):
  d.append(input())
  A.append(list(map(int, input().split())))
for i in range(K):
  plus=plus|set(A[i])
print(N-int(len(plus)))