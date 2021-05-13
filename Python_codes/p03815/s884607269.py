x=int(input())
a=x%11
if a==0:
    res=0
elif a<7:
    res=1
else:
    res=2
print((x//11)*2 + res)