def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    table = sorted(table)
    return table

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

A, B = map(int, input().split())

A_list = set(divisor(A))
B_list = set(divisor(B))

list = A_list & B_list

cnt = 1

for i in list:
    if is_prime(i):
        cnt += 1

print(cnt)