s,c=map(int,input().split())
result=0
if c>=2*s:
  result = s +(c-2*s)//4
else:
  result = c//2
print(result)
