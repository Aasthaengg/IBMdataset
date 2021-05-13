n=int(input())
i=1
result=1
while i**2<=n:
  result=max(result,i**2)
  i=i+1
print(result)