
n=int(input())
s=input()

#初期化
ind=1
while 2**ind<=n:
    ind+=1
s+="*"*(2**ind-n)
seg=[]
seg2=[]

from collections import deque
tmp=deque([s])
while len(tmp)>0:
    t=tmp.popleft()
    cnt=0
    for ss in t:
        if ss!="*":
            cnt=cnt|2**(ord(ss)-97)
    seg.append(cnt)
    seg2.append(t)
    if len(t)>1:
        tmp.append(t[:len(t)//2])
        tmp.append(t[len(t)//2:])

#セグ木が出来た！
#print(seg)
#print(seg2)

q=int(input())

def change(i,s):
    #i文字目をsに変更する
    #nの親は(n-1)//2
    #nの子は2n+1,2n+2
    global n,seg,ind
    ii=len(seg)-2**ind+i-1
    seg[ii]=2**(ord(s)-97)
    p=(ii-1)//2
    while 1:
        seg[p]=seg[2*p+1]|seg[2*p+2]
        if p==0:
            break
        p=(p-1)//2

    #print(seg)

from collections import deque


def count(l,r):
    global n,seg,s
    #nの親は(n-1)//2
    #nの子は2n+1,2n+2

    d = deque([(1,len(s),0)])
    ans=0

    while len(d)>0:
        tmp=d.popleft()
        #print(tmp)
        ll,rr,i=tmp[0],tmp[1],tmp[2]
        if l<=ll and rr<=r:
            ans=ans|seg[i]
        elif (ll<=l and l<=rr) or (ll<=r and r<=rr):
            d.append((ll,ll+(rr-ll)//2,2*i+1))
            d.append((ll+(rr-ll)//2+1,rr,2*i+2))

    return str(bin(ans)).count("1")


result=[]


for _ in range(q):
    b,i,c=map(str,input().split())
    if b=="1":
        #i文字目をcに変更
        change(int(i),c)
    else:
        #l文字目からr文字目までに含まれる数
        result.append(count(int(i),int(c)))

for item in result:
    print(item)










    
         
