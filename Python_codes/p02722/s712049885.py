n = int(input())

def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


def tester(n, k):
    if k == 1:
        return False

    temp = n
    while temp % k == 0:
        temp /= k

    if temp % k == 1:
        return True
    else:
        return False

answer = []
for i in (divisor(n - 1) + divisor(n)):
    if tester(n, i):
        answer.append(i)

print(len(answer))