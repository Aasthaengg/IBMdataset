a, b = map(int, input().split())
if a >= 13:
    fee = b
elif 6 <= a <= 12:
    fee = b // 2
else:
    fee = 0

print(fee)