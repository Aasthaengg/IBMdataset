K, A, B = map(int, input().split())

bisket = 1
money = 0

if B - A > 2:
    remain = K - A + 1
    bisket = A
    bisket += remain // 2 * (B - A)
    if remain % 2 == 1:
        bisket += 1
else:
    bisket += K

print(bisket)
