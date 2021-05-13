a, b, k = list(map(int, input().split()))
def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = set(table)
    return table
ablist = sorted(list(divisor(a) & divisor(b)),reverse=True)
print(ablist[k-1])