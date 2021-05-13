from collections import Counter
n=input()[::-1]

A=[]
num,point=0,1
for i in n:
    num +=int(i)*point
    num %=2019
    A.append(num)
    point *=10
    point %=2019

count=Counter(A)
ans=0
for i,j in count.items():
    if i==0:ans +=j*(j+1)//2
    else:ans +=j*(j-1)//2
print(ans)