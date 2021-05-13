N=int(input())
n=N
listm=[]
listn=[]
l=0
while n!=0:
  m=n%26
  listm.append(m)
  n=n//26
  l+=1

for i in range(l):
  try:
    if listm[i]<=0:
      listn.append(listm[i]+26)
      listm[i+1]-=1
    else:
      listn.append(listm[i])
  except IndexError:
    listn.append(listm[i])
    l=l-1
    exit

list_ans=[]
for i in range(N):
  try:
    ans=chr(listn[i]+96)
    list_ans.append(ans)
  except IndexError:
    break

ans=''
for i in range(l):
  ans=ans+list_ans[l-i-1]

print (ans)