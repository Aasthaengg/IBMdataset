N,A,B=map(int,input().split())

if(A>B):
  ans1=B
  ans2=max(0,A-(N-B))
else:
  ans1=A
  ans2=max(0,B-(N-A))
  
print(str(ans1)+" "+str(ans2))
