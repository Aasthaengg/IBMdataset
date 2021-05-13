N=int(input())

ans_list=[]
sgn=1
for i in range(100):
  if N%2==1:
    ans_list.append("1")
    N-=sgn
  else:
    ans_list.append("0")
    
  N//=2
  sgn*=-1
  if N==0:
    break
  
print("".join(reversed(ans_list)))