import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

ans = 0

def divisor(x):
    res = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i != x//i:
                res.append(i)
                res.append(x//i)
            else:
                res.append(i)   
    return res[1:]


ans += len(divisor(N-1))

div_N = divisor(N)

for num in div_N:
    tmp = N
    while tmp % num == 0:
        tmp //= num
    if tmp == 1:
        ans += 1
        continue    
    if (tmp-1) % num == 0:
        ans += 1
print(ans)