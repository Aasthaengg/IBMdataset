import sys
def input():
    return sys.stdin.readline()[:-1]
s=input()
n=len(s)
lst=[0]*(n+1)
lst[1]=1
if s[0]==s[1]:
    lst[2]=1
else:
    lst[2]=2

for i in range(2,n):
    if s[i-1]==s[i]:
        lst[i+1]=lst[i-2]+2
    else:
        lst[i+1]=lst[i]+1

print(lst[-1])