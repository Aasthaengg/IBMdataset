N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
num = 0
dif = 10000000

for n in range(N):
  C = T-H[n]*0.006
  if dif > abs(A-C):
    dif = abs(A-C)
    num = n+1
    
print(num)