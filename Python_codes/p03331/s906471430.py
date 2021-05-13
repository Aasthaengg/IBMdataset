N=int(input())

mini=float("inf")
for A in range(1,N):
  B=N-A
  sa=str(A)
  sb=str(B)
  sum_a=0
  sum_b=0
  for st in sa:
    sum_a += int(st)
  for st in sb:
    sum_b += int(st)
  mini= min(mini, sum_a+sum_b)  
  
print(mini)