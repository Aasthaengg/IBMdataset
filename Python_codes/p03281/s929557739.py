N = int(input())
ls = [i+1 for i in range(N)]

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
ii = 0
for i in ls:
    if i % 2== 0:
        continue
    else:
        if len(divisor(i)) == 8:
            ii += 1
print(ii)