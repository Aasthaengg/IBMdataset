n,l = map(int,input().split())

sumsum = sum(range(l,l+n))
if 0<l:
    print(sumsum - l)
elif l+n-1<0:
    print(sumsum -l-n+1)
else:
    print(sumsum)
