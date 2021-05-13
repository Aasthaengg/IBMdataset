s=input()
t=""
i=len(s)
five=["dream","erase"]
flag=0
while s!=t:
  if i>=7 and s[i-7:i]=="dreamer":
    t=s[i-7:i]+t
    i-=7
  elif  i>=6 and s[i-6:i]=="eraser":
    t=s[i-6:i]+t
    i-=6
  elif i>=5 and (s[i-5:i] in five):
    t=s[i-5:i]+t
    i-=5
  else:
    flag=1
    break
if flag==0:
  print("YES")
else:
  print("NO")