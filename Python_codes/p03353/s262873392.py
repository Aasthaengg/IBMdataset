s=input()
K=int(input())

s1list=[]
for i in range(len(s)):
  s1list.append((s[i],i))
s1list.sort()
#print(s1list)

cold=s1list[0][0]
sset=set()
for i in range(len(s1list)):
  c1,index=s1list[i]
  if cold!=c1 and len(sset)>=5:
    break
  else:
    cold=c1
  
  for j in range(5):
    sub=s[index:index+j+1]
    sset.add(sub)
    
slist=list(sset)
slist.sort()
print(slist[K-1])