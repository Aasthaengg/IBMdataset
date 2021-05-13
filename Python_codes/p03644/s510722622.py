#B - Break Number
N = int(input())

result = 0
for i in range(7):
    if 2**i <= N:
        result = i
    else:
        break
print(2**result)