N = int(input())

lis = []
for i in range(1,N):
  A = i 
  B = N -i
  lis.append(sum(map(int,str(A)))+sum(map(int,str(B))))

print(min(lis))
