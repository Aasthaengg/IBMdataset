N = int(input())
ListN=[0]
List = []
res =0
flag = True
mid =0
n =0
for i in range(N):
  k = int(input())
  n += k
  ListN.append(n)
  for j in range(k):
    List.append(list(map(int, input().split())))
#print(List)
for bits in range(2**N):
  mid=0
  flag= True
  for j in range(N):
    #print(bits,j,((bits>>j) & 1))
    if((bits>>j) & 1): 
      mid+= 1
      #print(ListN[j],ListN[j+1])
      for k in range(ListN[j],ListN[j+1]):
        mynum = bits
        #print(bits,List[k][0],(mynum>>List[k][0])&1, List[k][1])
        if ((mynum>>List[k][0]-1)&1) != List[k][1]:
          flag = False
          break
  #print(bits,flag,mid)
  if flag:
    res = max(res,mid)
print(res)