n = int(input())
if n % 2 == 1:
    print(0)
    exit()
n //= 2
acc = 0
while n >= 5:
    acc += n // 5
    n //= 5
print(acc)