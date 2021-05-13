import math
def yakusu(n):
    count = 0
    for i in range(1,int(math.sqrt(n))+1+1):
        if n % i == 0:
            count += 2
    return count
N = int(input())
c = 0
for i in range(1,N+1,2):
    if yakusu(i) == 8:
        c+=1

print(c)
