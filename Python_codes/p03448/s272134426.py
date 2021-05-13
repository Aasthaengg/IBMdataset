a=range(int(input())+1)
b=range(int(input())+1)
c=range(int(input())+1)
x=int(input())
res=0
import itertools
p=itertools.product(a,b,c)
for i in p:
    ans =500*i[0]+100*i[1]+50*i[2]
    if ans==x:res+=1
print(res)