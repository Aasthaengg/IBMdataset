s=input()
cnt=0
i=0
j=s[0]
n=len(s)
while True:
  for k in range(i+1,n):
    if s[k]!=j:
      cnt+=1
      j=s[k]
      i=k
      break
  else:break
print(cnt)