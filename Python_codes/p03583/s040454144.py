N = int(input())
ans = []
for h in range(1,3500):
  for n in range(1,3500):
    if (4*h*n - N*(h+n))>0 and (N*h*n)%(4*h*n - N*(h+n))==0:
        print(h,n,(N*h*n)//(4*h*n - N*(h+n)))
        exit()