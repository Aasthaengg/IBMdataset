from sys import stdin
N = int(stdin.readline().rstrip())
for h in range(1,3501):
    for n in range(1,3501):
        if (4*h*n-N*h-N*n) != 0:
            w = (N*h*n)/(4*h*n-N*h-N*n)
        else:
            continue
        if w.is_integer() and w > 0:
            print(h,n,int(w))
            break
    else:
        continue
    break