import math

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

def seikai(x):
    count = 0
    for i in range(n):
        count += math.ceil(a[i] / x) - 1

    if(count <= k):
        return 1
    else:
        return 0

l = 0
r = 10 ** 9
while(r - l > 1):
    temp = (r + l) // 2
    if(seikai(temp) == 1):
        r = temp
    else:
        l = temp

print(r)