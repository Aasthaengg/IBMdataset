n,p=map(int,input().split())
a=list(map(int, input().split()))
from math import factorial
o=0;e=0
for i in a:
    if i%2==0:e+=1
    else:o+=1
if p==0:
    odds=0
    for i in range(0,o+1,2):
        odds+=factorial(o)//factorial(i)//factorial(o-i)
else:
    odds=0
    for i in range(1,o+1,2):
        odds+=factorial(o)//factorial(i)//factorial(o-i)
print(odds*2**e)