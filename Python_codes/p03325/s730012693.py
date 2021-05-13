n = int(input())
a = list(map(int, input().split()))

ret = 0

for item in a:
    while True:
        if item % 2 == 0:
            ret += 1
            item //= 2
        else:
            break

print(ret)
