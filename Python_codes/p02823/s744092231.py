def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


n, a, b = map(int, input().split())
tables = [n] * 2
if is_even(a) and is_even(b):
    print(abs(a - b) // 2)
elif not is_even(a) and not is_even(b):
    print(abs(a - b) // 2)
else:
    print(min(abs(1 - a), abs(b - n)) + 1 + (b - a - 1) // 2)
