n = int(input())
if n==1:
    print(1)
    exit()
for i in range(1,10**5):
    if (i**2 > n):
        print((i-1)**2)
        exit()