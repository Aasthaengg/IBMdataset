N = int(input())


def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


A = divisor(N)
A = [i - 1 for i in A]

ans = 0
for a in A:
    if a == 0:
        continue
    if N // a == N % a:
        ans += a

print(ans)