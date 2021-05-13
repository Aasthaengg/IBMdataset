N=int(input())
alist=list(map(int,input().split()))
#print(alist)

slist=[0]
xlist=[0]
for i in range(N):
  slist.append(slist[-1]+alist[i])
  xlist.append(xlist[-1]^alist[i])
#print(slist)
#print(xlist)

ans_list=[0]*N
l,r=1,1
while(r<N):
  #check [l,r+1] is valid
  sum_lr=slist[r+1]-slist[l-1]
  xor_lr=xlist[r+1]^xlist[l-1]
  #print(l,r,sum_lr,xor_lr)
  if sum_lr==xor_lr:
    r+=1
  else:
    #print(l-1,r-1)
    ans_list[l-1]=r-1
    l+=1
#print(l-1,r-1)

for i in range(l-1,N):
  ans_list[i]=r-1
#print(ans_list)

answer=0
for i in range(N):
  answer+=ans_list[i]+1-i
  
print(answer)