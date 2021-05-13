s=input()

def sigma(n):
  return n*(n+1)//2

total=0
if s[0]=='>':
  cnt=s.find('<')
  if cnt==-1:
    cnt=len(s)
    s=''
  else:
    s=s[cnt:]
  total+=sigma(cnt)
  
flag=True
while flag:
  l=[]
  index1=s.find('>')
  if index1!=-1:
    for i in range(index1):
      l.append(s[i])
    s=s[index1:]
  else:
    l.extend(['<']*len(s))
    s=''
    flag=False
  index2=s.find('<')
  if index2!=-1:
    for i in range(index2):
      l.append(s[i])
    s=s[index2:]
  else:
    l.extend(['>']*len(s))
    s=''
    flag=False
  cnt1=l.count('>')
  cnt2=l.count('<')
  if cnt2<=cnt1:
    total+=sigma(cnt1)+sigma(cnt2-1)
  else:
    total+=sigma(cnt2)+sigma(cnt1-1)

print(total)