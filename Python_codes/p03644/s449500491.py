N = int(input())
kmax = 0
x = 1
for i in range(1,N+1):
    k = 0
    y = i
    while y%2==0:
        y = y//2
        k += 1
    if k>kmax:
        x=i
        kmax = k
print(x)