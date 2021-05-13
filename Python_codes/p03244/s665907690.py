n=int(input())
v=list(map(int,input().split()))
temp1=[]
temp2=[]
for i in range(0,n):
  if i%2==0:
    temp1.append(v[i])
  else:
    temp2.append(v[i])
count=0
from collections import Counter
c1=Counter(temp1)
values1,counts1=zip(*c1.most_common())
counts1=list(counts1)
mode1=counts1[0]
if len(counts1)>1:
  mode1s=counts1[1]
c2=Counter(temp2)
values2,counts2=zip(*c2.most_common())
counts2=list(counts2)
mode2=counts2[0]
if len(counts2)>1:
  mode2s=counts2[1]
if len(counts1)==1 and len(counts2)==1 and c1.most_common()[0][0]==c2.most_common()[0][0]:
  count=min(mode1,mode2)
elif c1.most_common()[0][0]==c2.most_common()[0][0]:
  if len(temp1)-mode1s>=len(temp2)-mode2s:
    count=len(temp1)-mode1+len(temp2)-mode2s
  else:
    count=len(temp2)-mode2+len(temp1)-mode1s
else:
  count=len(temp1)-mode1+len(temp2)-mode2
print(count)