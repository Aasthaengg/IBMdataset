import collections
n=int(input())
num=[]
l=[]
count=0
for _ in range(n):
    a=int(input())
    l.append(a)
l=collections.Counter(l)
for i in l.values():
    if i%2!=0:
        count+=1
print(count)