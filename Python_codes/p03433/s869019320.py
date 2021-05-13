n = int(input())
a = int(input())

while True:
    if n >= 500:
        n -= 500
    
    else:
        break

if a >= n:
    print('Yes')
else:
    print('No')