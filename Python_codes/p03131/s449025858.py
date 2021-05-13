k, a, b = map(int, input().split())
c = 1
if a + 2 >= b: print(c+k)
else:
    if k - (a+1) >= 0:
        k = k - (a+1)
        c = b
        c += (k//2)*(b-a) + k%2
        print(c)
    else:
        print(c+k)