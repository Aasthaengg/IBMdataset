x=int(input())
a=x%11
if a==0:
    cnt=0
elif 0<a and a<=6:
    cnt=1
else:
    cnt=2

print(x//11*2+cnt)