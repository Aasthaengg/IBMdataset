a,b=map(int,input().split())
check=0
for i in range(1,(b-a)+1):
  check+=i
print(check-b)
