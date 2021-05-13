N = int(input())
A = list(map(int,input().split()))
B = (10**5+1)*[0]
ans = 0

for a in A:
  if a<=10**5:
    B[a]+=1
  else:
    ans+=1

for n in range(10**5):
  if B[n]<n:
    ans+=B[n]
  elif n<B[n]:
    ans+=B[n]-n

print(ans)