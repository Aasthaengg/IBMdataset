import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def pop_cnt(n):
    return bin(n).count('1')


def f(n):
    cnt = 0
    while n != 0:
        n = n % pop_cnt(n)
        cnt += 1
    return cnt
 
n = int(readline())
x2 = list(readline().decode().rstrip())
x10 = int(''.join(x2), 2)

c = x2.count('1')
mod1 = x10 % (c + 1)
mod2 = x10 % (c - 1) if c-1 != 0 else 0

for i in range(n):
    ans = 0
    if x2[i] == '0':
        t = (mod1 + pow(2, n-i-1, c+1)) % (c+1)
    else:
        if c-1 != 0:
            t = (mod2 - pow(2, n-i-1, c-1)) % (c-1)
        else:
            print(0)
            continue
    
    ans = f(t) + 1
    print(ans)