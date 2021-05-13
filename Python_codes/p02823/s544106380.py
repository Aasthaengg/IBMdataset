N,A,B=map(int,input().split())

if abs(A-B) % 2 == 0:
  print(abs(A-B) // 2)
  exit()
  
if abs(A-B) == 1:
  print(min(max(A-1,B-1),max(N-A,N-B)))
  exit()
  
print(min(min(A-1,B-1),min(N-A,N-B))+1+(abs(A-B)-1)//2)