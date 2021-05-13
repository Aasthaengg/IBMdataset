def readinput():
    h,w=map(int,input().split())
    smat=[]
    for _ in range(h):
        smat.append(input())
    return h,w,smat

def main(h,w,smat):
    tmat=[]
    for _ in range(h):
        t=[0 for tt in range(w)]
        tmat.append(t)
    #print(tmat)
    for i in range(h):
        s=smat[i]
        l=0
        r=s.find('#',l)
        #print(i,l,r)
        while(r>=0):
            for k in range(l,r):
                tmat[i][k]=r-l
            l=r+1
            if (l>=w):
                break
            r=s.find('#',l)
            #print(i,l,r)
        else:
            for k in range(l,w):
                tmat[i][k]=w-l
        #print(tmat[i])
    maxt=0
    for j in range(w):
        u=0
        b=u
        while b<h:
            #print(b,j)
            while b<h and smat[b][j]=='.':
                b+=1
            for k in range(u,b):
                maxt=max(maxt, tmat[k][j]+b-u-1)
            u=b+1
            b=u

    return maxt

if __name__=='__main__':
    h,w,smat=readinput()
    ans=main(h,w,smat)
    print(ans)
