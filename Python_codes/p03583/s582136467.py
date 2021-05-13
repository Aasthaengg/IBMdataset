N = int(input())

for i in range(1,3500+1):
    for j in range(1,3500+1):
        h = i
        n = j
        
        low = 1
        high = 3500
        
        if N*n+N*h-4*h*n == 0:
            continue
        if N*h*n % (N*n+N*h-4*h*n) == 0:
            w = -N*h*n // (N*n+N*h-4*h*n)
            if w > 0:
                print(h,n,w)
                exit()
        
