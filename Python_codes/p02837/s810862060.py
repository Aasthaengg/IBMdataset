import itertools
N = int(input())
xys=[]
for i in range(N):
    A = int(input())
    xy = []
    for i in range(A):
        xy.append(list(map(int,input().split())))
    xys.append(xy)
#print('xys:', xys)  ############


#正直者1,  不親切0
a = [0,1]
Ls = list(itertools.product(a, repeat=N))
#print('Ls:', Ls)  ###########

mujun=[0]*(N+1)
count=0
ans=0
for L in Ls:
    #print('L:        ', L)  ###########
    flag=0
    hito=1
    #count=0
    count=sum(list(L))
    mujun=[0] + list(L)
    for i in L:
        #print('i:', i)    ###########
        if i==1:
            for xy in xys[hito-1]:
                #print('xy:', xy)  #########
                if xy[1] == 1:
                    if mujun[xy[0]]==0:
                        count=0
                        #print('mujuuuuuunnnnnnn!')
                        flag=1
                        break
                    #else:
                        #count+=1
                        #mujun[xy[0]]=1
                else:
                    if mujun[xy[0]]==1:
                        count=0
                        #print('mujuuuuuuuuuuuuuuuuuuuun!')   ###########
                        flag=1
                        break
                    #else:
                        #mujun[xy[0]]=-1


                #print('count:', count)  ###########
                #print('mujun:', mujun)  ###########
        hito+=1
    if flag==0:
        ans=max(ans,count)
    #print('ans:', ans)  ###########

#print('ans:', ans) ###########
print(ans)
