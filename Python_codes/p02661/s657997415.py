n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]    
ab.sort()

# min
if n%2==1:
    med1 = ab[n//2]
    amin=med1[0]
else:
    med1 = ab[(n-1)//2]
    med2 = ab[(n-1)//2+1]
    amin = (med1[0] + med2[0])

ab.sort(key=lambda x: x[1])

# max
if n%2==1:
    med1 = ab[n//2]
    amax=med1[1]
else:
    med1 = ab[(n-1)//2]
    med2 = ab[(n-1)//2+1]
    amax = (med1[1] + med2[1])

if n%2==1:
    print(amax-amin+1)
else:
    print(amax - amin + 1)