from collections import Counter

n=int(input())
nl=sorted(list(map(int,input().split())))
m=int(input())
ml=sorted(list(map(int,input().split())))

cnl=Counter(nl)
cml=Counter(ml)

ans="YES"

for i in cml.keys():
  if i  not in cnl.keys():
    ans="NO"
  else:
    if cml[i] > cnl[i]:
      ans="NO"
      break
      
print(ans)