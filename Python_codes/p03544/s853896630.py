memo = [int(0) for i in range(87)]
def l(n):
    global memo
    if memo[n]>0:
        return memo[n]
    if n == 0:
        memo[0]=2
        return 2
    elif n == 1:
        memo[1]=1
        return 1
    else:
        memo[n] = l(n-1)+l(n-2)
        return memo[n]
n = int(input())
print(l(n))