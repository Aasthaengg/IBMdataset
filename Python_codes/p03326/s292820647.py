N,M=map(int,input().split())

LPPP=[]
LPPM=[]
LPMP=[]
LPMM=[]
LMPP=[]
LMPM=[]
LMMP=[]
LMMM=[]
for i in range(N):
    x,y,z=map(int,input().split())
    LPPP.append(x+y+z)
    LPPM.append(x+y-z)
    LPMP.append(x-y+z)
    LPMM.append(x-y-z)
    LMPP.append(-x+y+z)
    LMPM.append(-x+y-z)
    LMMP.append(-x-y+z)
    LMMM.append(-x-y-z)
    
LPPP.sort(reverse=True)
LPPM.sort(reverse=True)
LPMP.sort(reverse=True)
LPMM.sort(reverse=True)
LMPP.sort(reverse=True)
LMPM.sort(reverse=True)
LMMP.sort(reverse=True)
LMMM.sort(reverse=True)
print(max(sum(LPPP[:M]),sum(LPPM[:M]),sum(LPMP[:M]),sum(LPMM[:M]),sum(LMPP[:M]),sum(LMPM[:M]),sum(LMMP[:M]),sum(LMMM[:M])))