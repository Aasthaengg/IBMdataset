N=int(input())
aN=list(map(int,input().split()))
dic={}
for a in aN:
  if a in dic:
    dic[a] += 1
  else:
    dic[a] = 1
ans=0
for k,v in dic.items():
  if k > v:
    ans +=v
  else:
    ans+=v-k
print(ans)