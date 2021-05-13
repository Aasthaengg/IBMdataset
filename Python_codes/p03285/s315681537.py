n = int(input())
for q in range(0, n, 7):
    if q == 0:
        continue
    if (n - q) % 4 == 0:
        print("Yes")
        exit(0)
print("No" if (n % 4 != 0) and (n % 7 != 0) else "Yes")