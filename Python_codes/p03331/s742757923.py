def f(x):
    a = 0
    while x != 0:
        a += x % 10
        x //= 10
    return a

N = int(input())

Min = 1 + f(N-1)
for i in range((N//2)-1):
    Min = min(Min, f(i+2) + f(N-i-2))

print(Min)
