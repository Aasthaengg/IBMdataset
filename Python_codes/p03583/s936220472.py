N = int(input())
max_int = 3500
for n in range(1,max_int+1):
  for w in range(1,max_int+1):
    a1 = N*n*w
    a2 = 4*n*w-w*N-N*n
    if a2<=0:continue
    if a1%a2==0 and a1//a2<=max_int:
      print(N*n*w//(4*n*w-w*N-N*n), n, w)
      exit()