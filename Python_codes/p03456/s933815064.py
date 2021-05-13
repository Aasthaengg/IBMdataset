a,b=map(str,input().split())

n=a+b
 
for i in range(int(n)//2):
  if i**2==int(n):
    ans="Yes"
    break
  else:
    ans="No"
print(ans)
