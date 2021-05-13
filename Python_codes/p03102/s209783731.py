N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i in range(N):
  A.append(list(map(int, input().split())))
           
count = 0
for i in range(N):
  if sum(list(map(lambda x,y: x*y, A[i], B)))+C > 0:
    count += 1
    
print(count)