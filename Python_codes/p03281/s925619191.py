import sys

def divisor(num):
    cnt = 0
    for i in range(1, n+1):
        if(num % i == 0):
            cnt += 1
    return cnt


n = int(input())
ans = 1

if n <= 105:
    if n == 105:
        print(1)
    else:
        print(0)
    sys.exit()

for i in range(106, n+1):
    if (divisor(i) == 8 and i % 2 == 1):
        ans += 1
print(ans)
