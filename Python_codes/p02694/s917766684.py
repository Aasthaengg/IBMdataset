X=int(input())
r=100
p=100
n=0
while X>p:
  n+=1
  p+=p//r
print(n)