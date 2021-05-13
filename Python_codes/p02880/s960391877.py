N = int(input())
ok = False
for n in range(1, 10):
    if N % n == 0 and 1 <= N // n <= 9:
        ok = True
        break
print('Yes' if ok else 'No')