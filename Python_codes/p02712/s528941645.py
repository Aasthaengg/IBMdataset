N = int(input())
a = int()
for i in range(1, N + 1):
    if i % 3 != 0 and i % 5 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                a = a + i
print(a)