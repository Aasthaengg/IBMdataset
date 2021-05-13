from math import factorial as f
n, m = map(int, input().split())
if abs(n-m)>1:
    print(0)
else:
    if n==m:
        print(f(n)*f(m)*2%(pow(10,9)+7))
    else:
        print(f(n)*f(m)%(pow(10,9)+7))