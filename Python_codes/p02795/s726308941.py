h=int(input())
w=int(input())
n=int(input())
if w>=h:
    re=int(n/w)
    if n%w>0:
        re+=1
else:
    re=int(n/h)
    if n%h>0:
        re+=1
print(re)