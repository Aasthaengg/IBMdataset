a,b,c,d,e,k=int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
l=[a,b,c,d,e]
f=0
for i in range(4):
    for j in range(i+1,5):
        d=abs(l[j]-l[i])
        if(d>k):
            f=1
            break
if(f==0):
    print('Yay!')
else:
    print(':(')