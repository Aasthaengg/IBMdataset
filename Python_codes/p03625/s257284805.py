n=int(input())
a=list(map(int,input().split()))

a.sort(reverse=True)

i1=-1
lena1=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        lena1=a[i+1]
        i1=i
        break
if i1==-1:        
    print(0)
elif i1+2<len(a)-1:        
    lena2=0
    for i in range(i1+2,len(a)-1):
#        if a[i]==a[i+1] and a[i]!=lena1:
        if a[i]==a[i+1] :
            lena2=a[i+1]
            break
    print(lena1*lena2)
else:
    print(0)

