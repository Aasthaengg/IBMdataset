N = int(input())
res = ''

while True:
    amari = N % 26
    if amari == 0:
        amari = 26
    res += chr(96 + amari)
    N -= amari
    if N == 0:
        break
    N //= 26

print(res[::-1])
