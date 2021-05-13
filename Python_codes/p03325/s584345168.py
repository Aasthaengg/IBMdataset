N=int(input())
A=[int(x) for x in input().split()]
score=0
for i in A:
  while i%2==0:
    i/=2
    score+=1
print(score)