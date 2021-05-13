from math import ceil
n=int(input())
k=ceil((2*n)**0.5)
if k*(k-1)//2!= n:
  print('No')
  exit()

S=[[] for _ in range(k)]
a=1
for i in range(k):
  for j in range(i+1, k):
    S[i].append(a)
    S[j].append(a)
    a+=1

print('Yes')
print(k)
for i in range(k):
  print(len(S[i]),*S[i])