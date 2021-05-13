k,a,b = map(int,input().split())
if b<=a+1:
    print(1+k)
else:
    n = (k-a+1)//2
    m = (k-a+1)%2
    print(n*(b-a)+m+a)