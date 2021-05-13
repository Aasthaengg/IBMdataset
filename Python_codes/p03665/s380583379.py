n,p = map(int, input().split())
lis = list(map(int, input().split()))

odd = [i for i in lis if i % 2==1]
even = [i for i in lis if i % 2 == 0]

if len(odd) == 0:
    if p == 0:
        print(2**n)
    else:
        print(0)
else:
    odd_m = len(odd)
    even_m = len(even)
    t1 = 2**even_m
    t2 = 2**(odd_m-1)
    print(t1*t2)