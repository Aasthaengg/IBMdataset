N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

min_degree = 10000

for i in range(len(H)):
  temp = T - H[i]*0.006
  if abs(A-temp) < min_degree:
    min_degree = abs(A-temp)
    ans = i+1
    
print(ans)