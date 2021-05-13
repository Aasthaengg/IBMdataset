N = int(input())
def f(n):
    k = N // n
    return n * k * (k+1) // 2
ans = f(1) - f(3) - f(5) + f(15)
print(ans)