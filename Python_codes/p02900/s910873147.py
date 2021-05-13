#1は含まれない
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

def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


A,B=map(int,input().split())
AL = divisor(A)
BL = divisor(B)
AB = list(AL & BL)
cnt = 1
for l in AB:
    if is_prime(l):
        cnt+=1

print(cnt)
