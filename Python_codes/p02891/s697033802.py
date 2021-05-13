s=input()
k=int(input())
n=len(s)
counter=1
allsame=0
samefirst=1
samelast=1
firstletter=''
lastletter='.'
for i in range(n):
  if s[i]!=s[0]:
    firstletter=s[i]
    samefirst=i
    break
  if i==n-1:
    allsame=1
for i in range(n):
  if s[n-i-1]!=s[n-1]:
    lastletter=s[n-i-1]
    samelast=i
    break
  if i==n-1:
    allsame=1
anstemp=0
previousletter=s[samefirst-1]
for i in range(samefirst,n-samelast+1):
  currentletter=s[i]
  if currentletter==previousletter:
    counter+=1
  else:
    anstemp+=counter//2
    counter=1
    previousletter=currentletter
if allsame==1:
  print((k*n)//2)
elif firstletter==lastletter:
  print(anstemp*k+samefirst//2+samelast//2+(k-1)*((samefirst+samelast)//2))
else:
  print((anstemp+samefirst//2+samelast//2)*k)