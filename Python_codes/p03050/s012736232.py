N=int(input())
ans=0

def partions(M):#Mの約数列 O(n^(0.5+e))
    import math
    d=[]
    i=1
    while math.sqrt(M)>=i:
        if M%i==0:
            d.append(i)
            if i**2!=M:
                d.append(M//i)
        i=i+1
    d.sort()
    return d

list=partions(N)
for i in range(0,len(list)//2):
    q=list[i]
    m=N//list[i]-1
    if m>q:
        ans+=m

print(ans)