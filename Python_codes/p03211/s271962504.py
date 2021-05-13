import math
s=str(input())
l=[]
for i in  range(0,len(s)-2):
    d=s[i:(i+3)]
    d=int(d)
    l.append(abs(753-d))
print(min(l))