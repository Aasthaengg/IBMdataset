x = int(input())
num = (x - 1) // 11 * 2 + 1
if x % 11 > 6 or x % 11 == 0:
    num += 1
print(num)