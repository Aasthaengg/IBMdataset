N,P = map(int,input().split())
A = list(map(int,input().split()))

odd = 0
for v in A:
    if  v % 2:
        odd += 1 
even = N-odd
if odd != 0:
    print((2**even)*int(2**(odd-1)))
else:
    if P == 0:
        print(2**N)
    else:
        print(0)