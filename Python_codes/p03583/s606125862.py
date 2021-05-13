N = int(input())
for n in range(1,3501):
    for w in range(1,3501):
        if 4*n*w-N*w-N*n <= 0:
            continue
        h = (N*n*w)/(4*n*w-N*w-N*n)
        if h.is_integer():
            print(int(h),n,w)
            exit()