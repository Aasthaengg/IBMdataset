from operator import itemgetter
n,w=map(int,input().split())
wv=[tuple(map(int,input().split())) for i in range(n)]
wv.sort(key=itemgetter(1),reverse=True)#reverse
wv.sort(key=itemgetter(0))
#print(wv)
w0=wv[0][0]
x=[[0],[0],[0],[0]]
for i in range(n):
    z=wv[i][0]-w0
    k=wv[i][1]+x[z][-1]
    l=len(x[z])
    if l*wv[i][0]<=w:
        x[z].append(k)
ma=0
l3=len(x[3])
l2=len(x[2])
l1=len(x[1])
l0=len(x[0])
for i in range(l3):
    for j in range(l2):
        d=w-i*(w0+3)-j*(w0+2)
        if d>=0:
            for k in range(l1):
                d=w-i*(w0+3)-j*(w0+2)-k*(w0+1)
                if d>=0:
                    ma_sub=x[3][i]+x[2][j]+x[1][k]+x[0][min(d//w0,l0-1)]
                    ma=max(ma,ma_sub)
                else:
                    break
        else:
            break

print(ma)