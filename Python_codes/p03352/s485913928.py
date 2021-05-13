N=int(input())
ans=[]
for i in range(1,32):
  for k in range(2,11):
    c=i**k
    if c<=N:
      ans.append(c)
print(max(ans))