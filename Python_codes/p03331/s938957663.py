N = int(input())

MIN = 100000000000000
for i in range(1,N):
  A = sum(map(int,list(str(i))))
  B = sum(map(int,list(str(N-i))))
  MIN = min(A+B,MIN)
  
print(MIN)
  
