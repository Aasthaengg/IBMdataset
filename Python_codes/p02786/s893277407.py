memo = {}
def f(n):
    if n==1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = 1+2*f(n//2)
    return memo[n]
print(f(int(input())))