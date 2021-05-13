n = int(input())
s = 0
while True:
    s += n % 10
    n = n // 10
    if n == 0:
        break

if s == 1:
    print(10)
else:
    print(s)