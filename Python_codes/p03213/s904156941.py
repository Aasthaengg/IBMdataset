import math
n = int(input())
lis = [0] * n
for i in range(2,n+1):
    now = i
    for j in range(2,math.ceil(math.sqrt(i))+1):
        while now % j == 0:
            now //= j
            lis[j-1] += 1
    if now != 1:
        lis[now-1] += 1

def num(l):
    return len(list(filter(lambda x: x >= l-1, lis)))

print(num(75) + num(25) * (num(3) -1) + num(15) * (num(5) - 1) + num(5) * (num(5) - 1) * (num(3) - 2) // 2)