N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
m = 1 
mindis = abs(A-(T-H[0]*0.006))
for i in range(1,N):
  cd = abs(A-(T-H[i]*0.006))
  if mindis > cd:
    m = i+1
    mindis = cd
print(m)