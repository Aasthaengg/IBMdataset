import sys
input=sys.stdin.readline
k=int(input())
e=k//2
if k%2==0:
    o=e
else:
    o=e+1
print(o*e)



