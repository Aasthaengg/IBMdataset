n = int(input())

if n == 0:
    print(0)
    quit()
base = []
while n != 1:
    if n % -2 == 0:
        base.append('0')
        n //= -2
    else:
        base.append('1')
        n -= 1
        n //= -2
base.append('1')
base.reverse()
ans = ''.join(base)
print(ans)