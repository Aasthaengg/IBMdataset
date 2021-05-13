n = int(input())
result = []
def check(x, y, remnant):
    return x % y == remnant

for i in range(1, n + 1):
    x = i
    if check(x, 3, 0):
        result.append(i)
        continue
    for j in range(len(str(x))):
        if check(x, 10, 3):
            result.append(i)
            break
        x //= 10
print(' ' + ' '.join(map(str, result)))