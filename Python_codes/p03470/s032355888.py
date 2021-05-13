#coding=utf-8
i=int(input())
rrr=[]
for d in range(i):
    r=[int(input())]
    rrr+=r
s=len(set(rrr))
print(s)