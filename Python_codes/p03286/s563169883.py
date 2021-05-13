n = int(input())
if n==0:
    print('0')
    exit(0)
i = 1
s = []
while n!=0:
    if n%2**i>0:
        s.append('1')
        n -= (-2)**(i-1)
    else:
        s.append('0')
    i += 1
print(''.join(s[::-1]))