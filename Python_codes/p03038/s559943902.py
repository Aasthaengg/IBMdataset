n,m=map(int,input().split())
number_dict=dict()
a=list(map(int,input().split()))
for i in a:
  if i in number_dict:
    number_dict[i]+=1
  else:
    number_dict[i]=1

for i in range(m):
  b,c=map(int,input().split())
  if c in number_dict:
    number_dict[c]+=b
  else:
    number_dict[c]=b
number_dict_sort=sorted(number_dict,reverse=True)
#print(number_dict_sort)
#print(number_dict)
ans=0
for i in number_dict_sort:
  #print(i,ans)
  if n-number_dict[i]>=0:
    n-=number_dict[i]
    ans+=i*number_dict[i]
  else:
    ans+=n*i
    break
print(ans)


