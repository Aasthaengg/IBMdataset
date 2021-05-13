n = int(input())
s = []
while n != 0:
    rem = n%2
    if rem < 0:
        rem += 2
    
    n = (n-rem)//(-2)
    s.append(str(0+rem))

if len(s) == 0:
    print(0)
else:
    print(''.join(s[::-1]))

