X = int(input())
if X==1:
    print(1)
else:
    cmax = 1
    for i in range(2,int(X**0.5)+1):
        k = 2
        while i**k<=X:
            cmax = max(cmax,i**k)
            k += 1
    print(cmax)