import math

k, s = [int(i) for i in input().split()]

kotae = 0

for i in range(k+1):
    for j in range(k+1):
        if(s-i-j >= 0 and s-i-j <= k):
            kotae += 1


print(kotae)