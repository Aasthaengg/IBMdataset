N, M = map(int, input().split())
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

tab = divisor(M)
ans = []
for i in tab:
    j = M // i
    if j >= N:
        ans += [i]
print(max(ans))