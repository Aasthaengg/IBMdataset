s = int(input())

ans, num = [0, 0, 10 ** 9, 1], 10 ** 9
if s % num == 0:
    ans += [0, s // num]
elif s % num != 0:
    ans += [num - s % num, s // num + 1]
print(*ans)
