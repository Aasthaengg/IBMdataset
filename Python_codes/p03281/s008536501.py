import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def make_divisors(n):
    # 約数のリストを返す
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


n = int(readline())
l = []
for i in range(n+1):
    if len(make_divisors(i)) == 8 and i % 2 == 1:
        l.append(i)
print(len(l))
