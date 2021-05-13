import math
N=int(input())
i=math.ceil(math.sqrt(N))
while True:
    if N%i == 0:
        break
    else:
        i -= 1
j = N // i
print(i-1+j-1)
