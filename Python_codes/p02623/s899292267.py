N, M, K = map(int,input().split())

A = list(map(int,input().split()))
A.insert(0, 0)
B = list(map(int,input().split()))
a = []
b = []

def nibun(L,l,r,target):

  wrk = -(-(l+r)//2)
  
#  print(l,r,target,wrk)
  
  if r == l:
    if r == len(L):
      return 0
    else:
      return wrk + 1
  
  if l == (len(L)-1):
    if L[wrk-1] > target:
      return wrk
    else:
      return 0

  if L[wrk] == target:
    return wrk+1

  elif L[wrk] > target:
    return nibun(L,l,wrk-1,target)

  else:
    return nibun(L,wrk,r,target)

  
s = 0
for i,e in enumerate(B):
  s += e 
  b.append(s)

s = 0
ans = 0
for i in range(len(A)):
#  print(i,'kaime')
#  print(s,i,A[i])
  s += A[i]
  if s > K:
    break
  else:  
    wrk = nibun(b,-1,len(b),K-s)
    
    ans=max(ans,i+wrk)
#    print('koko',s,wrk,ans)

print(ans)