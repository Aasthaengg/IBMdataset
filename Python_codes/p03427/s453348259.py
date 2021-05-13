n=int(input())
t=list(str(n))
cnt=0
for i in range(1,len(t)):
  if t[i]=="9":
    cnt=cnt+1
if cnt==len(t)-1:
  print(int(t[0])+9*cnt)
else:
  print(int(t[0])-1+9*(len(t)-1))