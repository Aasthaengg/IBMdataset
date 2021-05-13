N = int(input())
A = list(map(int, input().split(" ")))

count=0

for i in [j for j in range(N) if j%2==0]:
  if A[i]%2==1:
    count=count+1
    
print(count)