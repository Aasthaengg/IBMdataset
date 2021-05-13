# your code goes here
#allocation
def ca(n,k,w,b):
    cn=0
    m=0
    l=0
    #print(k)
    while l <n and cn<=k:
        d=0
        #print(l)
        while d<b and l<n:
          #  print(l)
            d+=w[l]
            l+=1
          #  print(l)
        if d>b:
    #        d-=w[l]
            l-=1
        cn+=1
 #       print(l)
#        print(n)
#        print(cn)
    #    print(k)
    if cn>k:
        return 1
    else:
        return -1
  #  print(d)
def bs(n,k,w,Mx,U):
    while Mx+1<U:
        t=U-Mx
        t//=2
        t+=Mx
 #       print(t)
        if ca(n,k,w,t)==-1:
            U=t
        else:
            Mx=t
  #      print(Mx)
    if ca(n,k,w,Mx)==-1:
        return Mx
    else:
        return U
n,k=(int(i) for i in input().split())
w=[int(input())]
#print(w)
Mx=w[0]
for i in range(1,n):
    w.append(int(input()))
    if w[i]>Mx:
        Mx=w[i]
a=n//k
if n%k!=0:
    a+=1
U=a*Mx
#print(w)
Mx=bs(n,k,w,Mx,U)
print(Mx)