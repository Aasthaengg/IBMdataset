n=input()
dic={}
for i in range(1,int(n)+1):
  wkstr=str(i)[0]+str(i)[len(str(i))-1]
  if wkstr in dic:
    dic[wkstr]+=1
  else:
    dic[wkstr]=1
ans=0
for key in dic.keys():
  revkey=key[len(key)-1]+key[0]
  if key==revkey:
    ans+=dic.get(key)*dic.get(revkey)
  else:
    ans+=dic.get(key)*dic.get(revkey,0)
print(ans)