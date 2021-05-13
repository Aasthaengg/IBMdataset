import sys
input = sys.stdin.readline

h,w=map(int,input().split())
s=[[] for i in range(h)]
for i in range(h):
    si=input()
    s[i]=si
"""
h,w=4,6
s=[['#', '.', '.', '#', '.', '.'], ['.', '.', '.', '.', '.', '#'], ['.', '.', '.', '.', '#', '.'], ['#', '.', '#', '.', '.', '.']]    
"""
ww=[[0]*w for i in range(h)]
#www=[[0]*w for i in range(h)]
www=[0]*w
for i in range(h):
    jsum=0
    jcnt=1
    jj=[0]*(w+1)
    for j in range(w):
        if s[i][j]==".":
#            www[i][j]=jcnt
            www[j]=jcnt
            if j<w-1 and s[i][j+1]=="#":
                jcnt+=1
            jsum+=1
        else:
#            print(jsum,jst,jed)
            if jsum!=0:
                jj[jcnt-1]=jsum
            jsum=0
    jcnt+=1
    jj[jcnt-1]=jsum
            
    for j in range(w):
        if s[i][j]==".":
#            ww[i][j]=jj[www[i][j]]
            ww[i][j]=jj[www[j]]
#    print(jj)
                
hh=[[0]*w for i in range(h)]
hhh=[0]*h
for j in range(w):
    isum=0
    icnt=1
    ii=[0]*(h+1)
    for i in range(h):
        if s[i][j]==".":
#            www[i][j]=jcnt
            hhh[i]=icnt
            if i<h-1 and s[i+1][j]=="#":
                icnt+=1
            isum+=1
        else:
#            print(jsum,jst,jed)
            if isum!=0:
                ii[icnt-1]=isum
            isum=0
    icnt+=1
    ii[icnt-1]=isum
            
    for i in range(h):
        if s[i][j]==".":
#            ww[i][j]=jj[www[i][j]]
            hh[i][j]=ii[hhh[i]]
#    print(jj)
            
ijmax=0
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            ijmax=max(ijmax,ww[i][j]+hh[i][j]-1)

print(ijmax)
                
