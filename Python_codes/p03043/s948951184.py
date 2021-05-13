import math
a=0
N, K = map(int,input().split())
for i in range(1, N+1):
    if i < K:
        a += (1/2)**(math.ceil(math.log2(K/i)))
    else:
        a = a + 1
a =a/N
print(a)