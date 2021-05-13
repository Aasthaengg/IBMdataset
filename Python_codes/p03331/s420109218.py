N = int(input())

def SumOfDigits(n):
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10
    return(s)

ans = 0

for i in range(1, N):
    j = SumOfDigits(i) + SumOfDigits(N-i)
    if ans > j:
        ans = j
    elif ans == 0:
        ans = j
    else:
        pass

print(ans)