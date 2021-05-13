n = int(input())

alp = 'abcdefghijklmnopqrstuvwxyz'

name = []

while n > 0:
    n -= 1
    name.append(alp[n % 26])
    n //= 26

name.reverse()

print(*name,sep='')