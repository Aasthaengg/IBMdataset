from collections import deque
H,W = map(int, input().split())#H行　　W列
L=[]
kuro=0
siro=0

for i in range(H):
    a=list(input())
    L.append(a)
    for i in a:
        if i=='#':
            kuro+=1
        else:
            siro+=1
#print(kuro,siro)
#print(L)
q=deque([[1,1]])
move=[[1,0],[-1,0],[0,1],[0,-1]]
num=0
s=False
while q:
    #print(q)
    for i in range(len(q)):
        b=q.popleft()
        #print(b)
        if b==[H,W]:
            s=True
        #    print(num)
            print(H*W-kuro-num-1)
            break
        for m in move:
         #  print(m)
            if 1<=b[0]+m[0]<=H and 1<=b[1]+m[1]<=W and L[b[0]+m[0]-1][b[1]+m[1]-1]=='.':
                L[b[0]+m[0]-1][b[1]-1+m[1]]='#'
                q.append([b[0]+m[0],b[1]+m[1]])
        #print(L)
    num+=1
#print(L)
#print(num)
if not s:
    print('-1')