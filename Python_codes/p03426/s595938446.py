import pprint
H,W,D=map(int,input().split())
table=[list(map(int,input().split())) for _ in range(H)]
Q=int(input())
query=[list(map(int,input().split())) for _ in range(Q)]
num=[]
distfrom1D=[]
cumldist=[0]*(H*W+1)
for i in range(H):
    for j in range(W):
        num.append([table[i][j],i,j])
num.sort(key=lambda x:x[0])
#print(num)
#for i in range()
cnt=0
"""
for i in range(D):
    buf=[0]
    for j in range(i,H*W-D,D):
        #print(i+j,i+j+D)
        buf.append(buf[len(buf)-1]+abs(num[j][1]-num[j+D][1])+abs(num[j][2]-num[j+D][2]))
    #print(buf)
    distfrom1D.append(buf)
#[1,1+D,]
#[2,2+D,]
#...
#[D,D+D,]
#pprint.pprint(distfrom1D)
for i in range(Q):
    l=query[i][0]
    r=query[i][1]
    row=((l%D)-1)%D
    col1 = (l // D)
    col2 = (r // D)
    if l%D==0:
        col1=col1-1
        col2=col2-1
    print(distfrom1D[row][col2]-distfrom1D[row][col1])
"""
#""l-r%D==0より""、各点考えられる固定の始点(1..D)から1,2,...,1+D,2+D,...,1+2D,2+2D,...の累積和をdpっぽく作れる
for i in range(1,H*W+1):
    if i//D>0:
        cumldist[i]=cumldist[i-D]+abs(num[i-D-1][1]-num[i-1][1])+abs(num[i-D-1][2]-num[i-1][2])
#print(cumldist)
for i in range(Q):
    l=query[i][0]
    r=query[i][1]
    print(cumldist[r]-cumldist[l])




