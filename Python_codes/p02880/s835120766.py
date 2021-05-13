n = int(input())
i = 1
while i * i <= n:
    if n % i == 0:
        j = n // i
        if i < 10 and j < 10:
            print("Yes")
            quit()
    i += 1
print("No")