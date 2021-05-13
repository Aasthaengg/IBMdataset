n=int(input())
a=[int(i) for i in input().split()]
a=sorted(a)
while(len(a)>1):
    d=(a[0]+a[1])/2
    a[0]=d
    a.pop(1)
    if(len(a)==1):
        break
print(a[0])