n = int(input())

i = 0
while True:
    if i*(i+1)//2 >= n:
        break
    i += 1

while True:
    print(i)
    n -= i
    i -= 1
    if n == 0:
        break
    if n - i <= 0:
        print(n)
        break
