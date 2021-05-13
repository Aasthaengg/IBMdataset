s=input()
a=int(s[0])
b=int(s[1])
c=int(s[2])
d=int(s[3])
arr=[b,c,d]
for i in range(8):
    x=i
    m=a
    k=''
    for j in range(3):
        if x&1:
            m+=arr[j]
            k+='+'
        else:
            m-=arr[j]
            k+='-'
        x=x>>1
    if m==7:
        print (s[0]+k[0]+s[1]+k[1]+s[2]+k[2]+s[3]+'='+'7')
        break