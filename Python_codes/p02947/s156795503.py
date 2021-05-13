N=int(input())
dic={}
for i in range(N):
  s=input()
  s=sorted(s)
  s=''.join(s)
  if s in dic:
    dic[s]+=1
  if s not  in dic:
    dic[s]=1
ans=0
for v in dic.values():
  ans+=v*(v-1)/2
print(int(ans))