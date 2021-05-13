H,W=map(int,input().split())
a=[0]*H
for i in range(H):
  a[i]=list(map(int,input().split()))
  
move_even = [ (0,1) ,(1,0) ]
move_odd  = [ (0,-1),(1,0) ]
cnt=0
ans_list=[]

for i in range(H):
  if i%2==0:  #偶数列は左から
    for j in range(W):
      for move in move_even:
        p = i+move[0]
        q = j+move[1]
        if 0<=p<=H-1 and 0<=q<=W-1:
          if a[i][j]%2==1:
            a[i][j] += -1
            a[p][q] +=  1
            ans_list.append([i+1,j+1,p+1,q+1])
            cnt+=1
            break                
  else: #奇数列は右から
    for j in range(W-1,-1,-1):
      for move in move_odd:
        p = i+move[0]
        q = j+move[1]
        if 0<=p<=H-1 and 0<=q<=W-1:
          if a[i][j]%2==1:
            a[i][j] += -1
            a[p][q] +=  1
            ans_list.append([i+1,j+1,p+1,q+1])
            cnt +=1
            break         
print(cnt)
for queue in ans_list:
  print(*queue)