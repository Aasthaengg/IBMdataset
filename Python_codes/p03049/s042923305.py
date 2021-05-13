N=int(input())
a,b,ba=0,0,0
ret = 0
for i in range(N):
  st = input()
  ret+=st.count('AB')
  if st[0]=='B' and st[-1]=='A':
    ba+=1
  elif st[0]=='B':
    b+=1
  elif st[-1]=='A':
    a+=1
if ba>0:
  ret+=ba-1
  if a>0 and b>0:
    ret+=2
    ret+=min(a-1,b-1)
  elif a==0 and b==0:
    ret+=0
  else:
    ret+=1
else:
  ret+=min(a,b)
print(ret)
