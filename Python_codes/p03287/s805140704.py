N,M = map(int,input().split())
A = list(map(int,input().split()))

R = [A[0]%M]


for i in range(1,N):
  R.append((R[-1]+A[i])%M)



import collections
c = collections.Counter(R)


ans = 0
for key in c:
  if key == 0:
    ans += (c[key]*(c[key]+1))/2
  else:
    ans += (c[key]*(c[key]-1))/2
  



print(int(ans))
