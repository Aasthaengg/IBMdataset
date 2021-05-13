s = int(input())

ans = [s]

while True:
    if s % 2 == 0:
        s //= 2
    else:
        s = 3 * s + 1
    if ans.count(s) != 0:
        ans.append(s)
        break
    else:
        ans.append(s)


print(len(ans))
