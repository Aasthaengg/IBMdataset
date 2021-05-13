from sys import stdin
N = int(stdin.readline().rstrip())
for h in range(1,3501):
    for n in range(1,3501):
        if 4*n*h == N*(n+h):
            continue
        w = N*h*n/(4*n*h-N*(n+h))
        if w.is_integer() == True and w>0:
            print(n,h,int(w))
            exit()