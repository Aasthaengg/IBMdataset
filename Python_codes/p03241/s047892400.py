import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

def divisor(num):
    res = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            res.append(i)
            res.append(num//i)
    return res

div = divisor(M)
div.sort(reverse=True)
for num in div:
    if num <= M//N:
        print(num)
        exit()