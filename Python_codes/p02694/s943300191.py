import math
x=int(input())
p=100
cnt=0
while x>p:
    p+=p//100
    cnt+=1
print(cnt)
