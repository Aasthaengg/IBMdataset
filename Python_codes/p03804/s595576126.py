n,m=list(map(int,input().split()))
N=[list(input()) for _ in range(n)]
M=[list(input()) for _ in range(m)]

for i in range(n-m+1):
  for j in range(n-m+1):
    count = 0
    for k in range(m):
      if N[i+k][j:j+m] == M[k][:]:
        count += 1
    if count == m:
      print("Yes")
      exit()
    
print("No")