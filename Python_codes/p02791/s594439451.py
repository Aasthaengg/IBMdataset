N=int(input())
A=[int(x) for x in input().split()]
score=0
min_val=A[0]
for i in A:
  if i<=min_val:
    score+=1
    min_val=i
print(score)