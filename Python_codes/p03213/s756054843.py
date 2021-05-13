n=int(input())
e=[0 for i in range(n+1)]
for i in range(2,n+1):
  for j in range(2,i+1):
    if i==1:
      break
    while i%j==0:
      i//=j
      e[j]+=1

def num(k):
  ret=0
  for i in range(n):
    if e[i]>=k-1:
      ret += 1
  return ret
print(num(75) + num(25) * (num(3) - 1) + num(15) * (num(5) - 1) + num(5) * (num(5) - 1) * (num(3) - 2) // 2)