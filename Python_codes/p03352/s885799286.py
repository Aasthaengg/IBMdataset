n = int(input())
if  n == 1 or n == 2 or n == 3:
    print(1)
    exit()
while n > 0:
    for i in range(n):
        for j in range(2, 10):
            if n == i**j:
                print(n)
                exit()
    n -= 1