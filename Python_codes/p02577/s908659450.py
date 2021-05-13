n = int(input())

d = 0
while True:
    d += n // 10
    n -= d*10

    if n < 10:
        d += n
        break

if not d % 9:
    print("Yes")
else:
    print("No")
