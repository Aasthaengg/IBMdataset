N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(N):
  B.append(A[i]-(i+1))
B.sort()
lb = [B[N//2]-1,B[N//2]]

sad = float("inf")
for b in lb:
  c = 0
  for j in range(N):
    c += abs( A[j]-(b+j+1) )
  sad = min(sad,c)
print(sad)  