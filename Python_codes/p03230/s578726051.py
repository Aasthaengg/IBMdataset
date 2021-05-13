N=int(input())
cN=N

d=1
while N%2==0:
  N//=2
  d+=1

k=-1
for i in range(1,int(N**0.5)+1):
  if N%i==0:
    if abs(i*(2**d)-N//i)==1:
      k=max(i*(2**d),N//i)
      break
    elif abs((N//i)*(2**d)-i)==1:
      k=max((N//i)*(2**d),i)
      break

if k==-1:
  print("No")
else:
  print("Yes")
  print(k)
  S=[[] for _ in range(k)]
  n=0
  for j in range(k):
    for i in range(1,k-j):
      S[j].append(n+i)
      S[i+j].append(n+i)
    n+=i
  
  for i in range(k):
    print(k-1," ".join(map(str,S[i])))
