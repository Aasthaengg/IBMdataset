memo = {}
def f(x):
    if x==0:
        return 2
    if x==1:
        return 1
    if x in memo:
        return memo[x]
    memo[x] = f(x-1)+f(x-2)
    return memo[x]
print(f(int(input())))