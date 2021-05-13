k,a,b = map(int,input().split())
ans0 = 1+k
#a<bの時のみ交換を行う。1>>aになるまで加算し、そのあとはa-bを繰り返す。

if a+2>=b:
    print(1+k)
else:
    q=(k-a+1)//2
    if q==0:
        print(1+k)
    else:
        print(1+(k-2*q)+q*(b-a))