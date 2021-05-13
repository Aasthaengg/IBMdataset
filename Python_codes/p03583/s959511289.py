N = int(input())
solved = False
for h in range(1,3501):
    for n in range(1,3501):
        if 4*h*n-N*(h+n)>0 and (N*h*n)%(4*h*n-N*(h+n))==0:
            print(h,n,(N*h*n)//(4*h*n-N*(h+n)))
            solved = True
            break
    if solved:
        break