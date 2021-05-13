D, N = map(int, input().split())

count = 1
num = 100 ** D
while count != N:
    num += 100 ** D
    if num % (100 ** (D + 1)) == 0:
        continue
    else:
        count += 1

print(num)