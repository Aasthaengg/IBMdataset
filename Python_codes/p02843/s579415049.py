x = int(input())
num = x // 100
rem = x % 100
print('0' if rem > num*5 else '1')