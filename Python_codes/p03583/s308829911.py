N = int(input())
for h in range(1,3500):
    for n in range(1,3500):
        if 4*h*n-N*h-N*n != 0 and N*h*n%(4*h*n-N*h-N*n) == 0 and 0 < N*h*n//(4*h*n-N*h-N*n):
            print(h,n,N*h*n//(4*h*n-N*h-N*n))
            break
    else:
        continue
    break