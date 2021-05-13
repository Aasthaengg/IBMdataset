N = int(input())
for h in range(1,3501):
    for n in range(1,3501):
        t1 = 4 * h * n
        t2 = N * (h+n)
        if t1 != t2:
            temp = (N*h*n) / (t1-t2)
            if temp.is_integer():
                if temp > 0:
                    print(h,n,int(temp))
                    break
    else:
        continue
    break