N=int(input())
pr=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
l=[0]*15
for i in range(1,N+1):
    for j in range(15):
        while 1:
            if i%pr[j]==0:
                i//=pr[j]
                l[j]+=1
            else:
                break
a,b,c,d,e=0,0,0,0,0
for i in l:
    if i>=2:
        a+=1
    if i>=4:
        b+=1
    if i>=14:
        c+=1
    if i>=24:
        d+=1
    if i>=74:
        e+=1
print((a-2)*b*(b-1)//2+c*(b-1)+d*(a-1)+e)