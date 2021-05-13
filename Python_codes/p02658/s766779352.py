n = int(input())
a= list(map(int,input().split()))
c = 1
if 0 in a:
    print(0)
else:
    for x in a:
        if x >10**18:
            print(-1)
            break
        else:
            c*=x
            if c >10**18:
                print(-1)
                break
    else:
        print(c)