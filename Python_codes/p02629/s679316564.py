n = int(input())
c = " "
while n:
    if n % 26 == 0:
        c += 'z'
        n -= 1
    else:
        c += chr((n % 26) + ord('a') - 1)
    n //= 26
print(c[::-1])
