k,a,b = map(int,input().split())
if a >= b or a + 2 >= b:
    print(k+1)
else:
    if k+1 <= a:
        print(k+1)
    else:
        k = k-a+1
        c = k%2
        d = k//2
        print(a+(b-a)*d+c)