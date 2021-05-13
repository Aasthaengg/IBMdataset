a_list=[]
b_list=[]
while True:
  a,b = map(int, input().split())
  if a == 0 and b == 0: 
    break
  a_list.append(a)
  b_list.append(b)


  

for (alist, blist) in zip(a_list,b_list):
  if alist < blist:
    print(alist, blist)
  else:
    print(blist,alist)
  
