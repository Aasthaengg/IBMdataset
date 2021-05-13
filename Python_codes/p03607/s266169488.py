from collections import Counter
n=int(input())
a=[]
for _ in range(n):
    a.append(input())
c=Counter(a)
tmp=[]
for k,v in c.items():
    if v%2!=0: 
        tmp.append(k)
print(len(tmp))