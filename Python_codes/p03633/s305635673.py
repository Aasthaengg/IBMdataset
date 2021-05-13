from math import gcd
N,*T = map(int, open(0).read().split())
if N == 1:
    print(T[0])
else:
    temp = (T[0]*T[1]) // gcd(T[0],T[1])
    for i in range(2,N):
        temp = (temp*T[i]) // gcd(temp,T[i])
    print(temp)