n = int(input())
a = [n]
cnt = 1
while True:
    if a[-1] % 2 == 0:
        x = [a[-1] // 2]
        if set(x) & set(a) == set():
            a.append(x[0])
        else:
            cnt += 1
            break
    else:
        x = [a[-1] * 3 + 1]
        if set(x) & set(a) == set():
            a.append(x[0])
        else:
            cnt += 1
            break
    cnt += 1
print(cnt)
