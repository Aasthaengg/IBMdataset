N,M = map(int,input().split())
A = list(map(int,input().split()))

R = [A[0]%M]


for i in range(1,N):
  R.append((R[-1]+A[i])%M)

k = set(R)
dic = {i:0 for i in k}
for item in R:
  dic[item]+=1
  
  
ans = 0
if 0 in dic:
  ans = (dic[0]*(dic[0]+1))/2


for i in k:
  if i !=0 :
    ans += (dic[i]*(dic[i]-1))/2
    

    
print(int(ans))
