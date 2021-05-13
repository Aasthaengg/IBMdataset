N = int(input())
for h in range(1,3501):
    for n in range(1,3501):
        val = (4*n*h - N*n - N*h)
        if val > 0:
            if (N*n*h) % val == 0:
                print(h,n,(N*n*h)//val)
                exit()
            
