N = input()
s = []
for i in range(int(N)):
  s.append(input())
M = input()
t = []
for i in range(int(M)):
  t.append(input())
  
strdict = dict()
strset = set()
strset.add('')
strdict['']=0

for str in s:
  if str in strset:
    strdict[str]+=1
  else:
    strset.add(str)
    strdict[str]=1
for str in t:
  if str in strset:
    strdict[str]-=1
  else:
    strset.add(str)
    strdict[str]=-1

maxval=0
for str in strset:
  if maxval < strdict[str]:
    maxval=strdict[str]
print(maxval)