n,h,m = map(int,input().split())
answer = 0
a = 0
b = 0
for i in range(n):
  a,b = map(int,input().split())
  if(a-h>=0 and b-m>=0):
    answer +=1
print(answer)