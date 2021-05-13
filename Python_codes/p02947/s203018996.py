import sys
input=sys.stdin.readline

n=int(input())
dic=[]
for i in range(n):
    dic.append(sorted(list(input().rstrip())))
dic=sorted(dic)

from math import factorial

ans=0
temp=1
for i in range(1,n):
    if dic[i]==dic[i-1]:
        temp+=1
    else:
        if temp>=2:
            ans+=(factorial(temp)//(2*factorial(temp-2)))
        temp=1

if temp>=2:
    ans+=(factorial(temp)//(2*factorial(temp-2)))

print(ans)