from collections import deque
n,k=map(int,input().split())
l=list(map(int,input().split()))
plus=[]
minus=deque()
for i in l:
    if i<0:
        minus.appendleft(abs(i))
    elif i>0:
        plus.append(i)
    else:
        k-=1
minus=list(minus)
lenp=len(plus)
lenm=len(minus)
if k==0:
    print(0)
else:
    tcounter=[]
    if lenp>=k:
        tcounter.append(plus[k-1])
        if lenm>=k:
            for i in range(1,k):
                tcounter.append(min(plus[k-1-i],minus[i-1])+plus[k-1-i]+minus[i-1])
            tcounter.append(minus[k-1])
        else:
            for i in range(1,lenm+1):
                tcounter.append(min(plus[k-1-i],minus[i-1])+plus[k-1-i]+minus[i-1])
    else:
        if lenm>=k:
            for i in range(k-lenp,k):
                tcounter.append(min(plus[k-1-i],minus[i-1])+plus[k-1-i]+minus[i-1])
            tcounter.append(minus[k-1])
        else:
            for i in range(k-lenp,lenm+1):
                tcounter.append(min(plus[k-1-i],minus[i-1])+plus[k-1-i]+minus[i-1])
                
            
         
    print(min(tcounter))