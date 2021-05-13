N=int(input())
A=[int(x) for x in input().split()]
x=len(set(A))
answer=x
if x%2==0:
  answer-=1
print(answer)