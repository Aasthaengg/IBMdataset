N = int(input())
flag = 0

for h in range(1,3500):
    for n in range(1,3500):
        x = 4*h*n
        y = N*(h+n)
        if x<=y:
            continue
        tmp = (N*h*n)/(x-y)
        if tmp.is_integer():
            print(h,n,int(tmp))
            flag = 1
            break
    if flag == 1:
        break
