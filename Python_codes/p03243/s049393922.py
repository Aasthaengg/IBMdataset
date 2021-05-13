n=int(input())

while(1):
  a=str(n)
  if a.count(a[0])==3:
    break
  n+=1
print(n)