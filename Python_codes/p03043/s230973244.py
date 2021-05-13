N,K = map(int,input().split())

from math import ceil
cnt = 0
for i in range(1,N+1):
    a = ceil(K/i)
    if bin(a).count("1") == 1:
        b = a.bit_length()-1
    else:
        b = a.bit_length()
    cnt += (1/N)*(0.5**b)
print(cnt)