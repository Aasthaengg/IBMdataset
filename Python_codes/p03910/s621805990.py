n = int(input())

k = 1
i = 1
while k < n:
    i += 1
    k += i

while n > i:
    print(i)
    n -= i
    i -= 1
print(n)