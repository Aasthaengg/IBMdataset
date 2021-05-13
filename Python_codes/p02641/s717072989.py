x,n = map(int,input().split())
if n == 0:
    print(x)
else:
    p = list(map(int,input().split()))
    absolute = list(map(lambda i:abs(i-x),p))
    if 0 not in absolute:
        print(x)
    else:
        ab = set(p)
        i = 1
        while i < 100:
            if absolute.count(i) == 2:
                i += 1
            else:
                opt = set([x-i,x+i])
                ans = opt - ab
                break

        print(min(ans))
