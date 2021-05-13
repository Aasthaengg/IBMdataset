A,B,C=map(int,input().split())
ms=[0]*B
i=1
ans='NO'
while True:
  m=A*i%B
  if m==C:
    ans='YES'
    break
  else:
    if ms[m]==0:
      ms[m]=1
    else:
      break
  i+=1
  pass
print(ans)