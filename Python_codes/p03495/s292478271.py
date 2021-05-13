N,K=map(int, input().split())
A=list(map(int, input().split()))

from collections import Counter

AL=Counter(A)
AL= sorted(AL.items(), key=lambda x:x[1])
n=len(set(A))-K

sum=0
for i in range(n):
  sum+=AL[i][1]
print(sum)