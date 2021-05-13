n = int(input())
cnt = 0

for i in range(3,n):
  for j in range(1,n//i+1):
    if i * j < n:
      cnt +=1
      
print(cnt+n-1+(n-1)//2)