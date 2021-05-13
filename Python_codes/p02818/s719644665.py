A,B,K=map(int,input().split())
if A>K:
  print(str(A-K)+" "+str(B))
elif A+B>K:
  print(str(0)+" "+str(A+B-K))
else:
  print("0 0")