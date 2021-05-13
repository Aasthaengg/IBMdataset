# 1行目
p_str=input().split()
(N,K)=[int(n) for n in p_str]
# 2行目
p_str=input().split()
p_int=[int(n) for n in p_str]
(A,B)=(1,1)
for i in range(N-K):
  B=p_int[i]
  A=p_int[i+K]
  #  print(B,A,i)
  if B < A :
    print("Yes")
  else:
    print("No")
    
