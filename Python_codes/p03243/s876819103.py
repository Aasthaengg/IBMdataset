n = int(input())
i = int(n / 111)
if n % 111 != 0:
    i += 1
print(i * 111)
