# coding: utf-8
# Your code here!
n,m,d=map(int,input().split())

if n>=2*d:
    expe=(n-2*d)*2+2*d if d!=0 else n
elif n>=d:
    expe=2*(n-d)
else:
    expe=0
#print(expe)
print((expe/n**2)*(m-1))
