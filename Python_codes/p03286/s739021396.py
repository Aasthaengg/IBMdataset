n=int(input())

if n==0:
    print(0)
    exit(0)

pos=[0]*50
neg=[0]*50

def rec(x):
    if x>0:
        m=1
        while 4**m-1<3*x:
            m+=1
        
        pos[m-1]=1
        rec(x-4**(m-1))
    elif x<0:
        m=1
        while -2*(4**m-1)>3*x:
            m+=1
        
        neg[m-1]=1
        rec(x+2*(4**(m-1)))
    else:
        return

rec(n)

s=''
for i in range(100):
    if i%2==0:
        s=str(pos[i//2])+s
    else:
        s=str(neg[(i-1)//2])+s

i=0
while s[i]=='0':
    i+=1

print(s[i:])
