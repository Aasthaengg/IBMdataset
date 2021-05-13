h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
for i in range(h):
    for j in range(w):
        a[i][j]%=2
#print(a)
#do a snake traversel
hold=0
ans=[]
for i in range(h):
    if i&1:
        for j in range(w-1,-1,-1):
            #print(i,j,end=' curr \n')
            if hold:
                if a[i][j]:
                    a[i][j]=0
                    hold=0
                else:
                    if j==0 and i!=h-1:
#                        print(i,j,i+1,j)#move down
                        ans.append((i+1,j+1,i+2,j+1))
                    elif j>0:
#                        print(i,j,i,j-1)#move left
                        ans.append((i+1,j+1,i+1,j))
            else: #u r holding nothing 
                if a[i][j]:
                    hold=1
                    a[i][j]=0
                    if j==0 and i!=h-1:
 #                       print(i,j,i+1,j)#move down
                        ans.append((i+1,j+1,i+2,j+1))
                    elif j>0:
  #                      print(i,j,i,j-1)#move left
                        ans.append((i+1,j+1,i+1,j))
    else:
        for j in range(w):
            if hold:
                if a[i][j]:
                    a[i][j]=0
                    hold=0
                else:
                    if j==w-1 and i!=h-1:
   #                     print(i,j,i+1,j)#move down
                        ans.append((i+1,j+1,i+2,j+1))
                    elif j!=w-1:
    #                    print(i,j,i,j+1)#move right
                        ans.append((i+1,j+1,i+1,j+2))
            else:
                if a[i][j]:
                    hold=1
                    a[i][j]=0
                    if j==w-1 and i!=h-1:
     #                   print(i,j,i+1,j)#move down
                        ans.append((i+1,j+1,i+2,j+1))
                    elif j!=w-1:
      #                  print(i,j,i,j+1)#move right
                        ans.append((i+1,j+1,i+1,j+2))
print(len(ans))
for i in ans:
    print(' '.join(map(str,i)))
#print(a,end=' updated\n')    
