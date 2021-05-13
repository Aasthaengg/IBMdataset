import sys
input=sys.stdin.readline
n,a,b=map(int,input().split())
v_list=list(map(int,input().split()))
v_list.sort(reverse=True)
x=v_list[a-1]
print(sum(v_list[:a])/a)
import math
if v_list[0]==x:
    count=0
    for i in range(n):
        if v_list[i]==x:
            count+=1
    ans=0
    for i in range(a,min(b,count)+1):
        ans+=math.factorial(count)//(math.factorial(i)*math.factorial(count-i))
    print(ans)
else:
    counta=0
    for i in range(a):
        if v_list[i]==x:
            counta+=1
    count=0
    for i in range(n):
        if v_list[i]==x:
            count+=1
    ans=math.factorial(count)//(math.factorial(counta)*math.factorial(count-counta))
    print(ans)
