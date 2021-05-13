a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for ia in range(0, a + 1):
    for ib in range(0, b + 1):
        for ic in range(0, c + 1):
            if 500 * ia + 100 * ib + 50 * ic == x:
                count += 1

print(count)
