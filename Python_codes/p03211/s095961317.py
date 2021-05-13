n=input()

ans=753
for i in range(len(n)-2):
  a=int(n[i:i+3])
  if a==753:
    print(0)
    exit()
  b=abs(753-a)
  ans=min(b,ans)
  
print(ans)
  
