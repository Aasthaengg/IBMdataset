A, B, K = map(int, input().split())

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

print(sorted(list(set(divisor(A)) & set(divisor(B))), reverse=True)[K-1])
