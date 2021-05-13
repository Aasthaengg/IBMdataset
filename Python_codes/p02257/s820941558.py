from sys import stdin
def isPrime(x):
    if x == 2: return 1
    elif x % 2 == 0: return 0
    return pow(2, x - 1, x) == 1
n = int(stdin.readline())
cnt = 0
for i in range(0, n):
    cnt += isPrime(int(stdin.readline()))
print(cnt)