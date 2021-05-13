n = int(input())
lst = []
while n > 0:
    lst.append(n % 10)
    n //= 10
print(lst.count(2))
