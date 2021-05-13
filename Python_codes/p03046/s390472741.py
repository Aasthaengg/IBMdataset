m,k=map(int,input().split())
if k>=2**m:
    print(-1)
elif m==0:
    print('0 0')
elif m==1:
    if k==0:
        print('0 0 1 1')
    else:
        print(-1)
elif k<2**m:
    l=[i for i in range(2**m)]
    l.remove(k)
    l_=l.copy()
    l_ = l_ + [k] + l_[::-1] + [k]
    print(' '.join(map(str,l_)))
else:
    print('-1')