H,W,D=map(int,input().split())

board_dic={}
for i in range(H):
  array=list(map(int,input().split()))
  for j in range(W):
    num=array[j]
    board_dic[num]=(i+1,j+1)
#print(board_dic)  
  
dslist=[]
for i in range(1,D+1):
  dl=[0]
  for j in range(1,10**9):
    if i+j*D>H*W:
      break
    x1,y1=board_dic[i+(j-1)*D]
    x2,y2=board_dic[i+j*D]
    dist=abs(x2-x1)+abs(y2-y1)
    dl.append(dl[-1]+dist)
  dslist.append(dl)
#print(dslist)    

Q=int(input())
for i in range(Q):
  l,r=map(int,input().split())
  mod=(l-1)%D
  print(dslist[mod][(r-mod-1)//D]-dslist[mod][(l-mod-1)//D])