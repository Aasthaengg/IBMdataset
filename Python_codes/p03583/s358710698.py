import math

N = int(input())
for h in range(math.ceil(N/4),3500+1):
    buff = 4/N-1/h
    if buff==0:
        continue
    for n in range(math.ceil(1/buff),3500+1):
        #print(h,n)
        if 4*h*n-N*h-n*N!=0:
            if (N*h*n)%(4*h*n-N*h-n*N) ==0:
                print(h,n,int(N*h*n/(4*h*n-N*h-n*N)))
                exit()
print("not found")