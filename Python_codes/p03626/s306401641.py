N = int(input())
S_1 = input()
S_2 = input()

is_vertical = []

i = 0
while i < N:
    if i < N - 1 and S_1[i] == S_1[i + 1]:
        is_vertical.append(False)
        i += 2
    else:
        is_vertical.append(True)
        i += 1

res = 3 if is_vertical[0] else 6

for i in range(1, len(is_vertical)):
    if is_vertical[i] and is_vertical[i - 1]:
        res *= 2
    elif is_vertical[i] and not is_vertical[i - 1]:
        res *= 1
    elif not is_vertical[i] and is_vertical[i - 1]:
        res *= 2
    else:
        res *= 3

print(res % (10 ** 9 + 7))
