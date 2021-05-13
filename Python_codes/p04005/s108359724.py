a = list(map(int,input().split()))

a.sort()

if a[2] == 0:
    print(0)
    exit()
m = a[0]*a[1]
n = a[2]//2
print(abs(m*n-m*(a[2]-n)))