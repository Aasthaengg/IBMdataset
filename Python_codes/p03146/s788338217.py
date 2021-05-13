s=int(input())
a=[s]
res=0
while True:
    tmp=0
    if a[res]%2==0:
        tmp=a[res]/2
    else:
        tmp=3*a[res]+1
    res+=1
    if tmp in a:
        break
    a.append(tmp)
print(res+1)