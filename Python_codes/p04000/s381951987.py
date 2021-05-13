H,W,N=map(int,input().split())

allcase=(H-2)*(W-2)

abset=set()
for _ in range(N):
  a,b=map(int,input().split())
  abset.add((a-1,b-1))
#print(abset)

memo={}
def count_black(x,y):
  if (x,y) in memo:
    return memo[(x,y)]
  
  num_black=0
  for ii in range(3):
    for jj in range(3):
      if (x+ii,y+jj) in abset:
        num_black+=1
        
  memo[(x,y)]=num_black
  return num_black

case_list=[0]*10
for a,b in abset:
  for j in range(3):
    if a-j<0 or H-2<=a-j:
      continue    
    for k in range(3):
      if b-k<0 or W-2<=b-k:
        continue
      count_black(a-j,b-k)
#print(memo)  

case_list=[0]*10
for v in memo.values():
  case_list[v]+=1
case_list[0]=allcase-sum(case_list[1:])
#print(case_list)

for i in range(10):
  print(case_list[i])