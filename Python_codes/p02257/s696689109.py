n = int(input())
ls = [int(input()) for _ in range(n)]


def judge(n):
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0:
        return 0
    i = 3
    while i <= n/i:
        if n%i == 0:
            return 0
        else:  
            i += 2
    return 1

print(sum(map(judge, ls)))
