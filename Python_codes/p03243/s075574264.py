n = int(input())

if n % 111 ==0:
    print(n)
    exit()

while n % 111 != 0:
    n += 1
    if n % 111 == 0:
        print(n)
        exit()