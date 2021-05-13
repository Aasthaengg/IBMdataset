a, b = map(int, input().split())

a -= 1
b -= 1

ans = [[ '#' for _ in range(100)]]

for i in range(1, 49):
    temp = [ '#' for _ in range(100)]
    if a > 0:
        if i % 2 != 0:
            for j in range(min(a, 49)):
                temp[2 * j + 1] = '.'
                a -= 1
        else:
            ans.append(temp)
            continue
    else:
        break
    ans.append(temp)

ans.append([ '#' for _ in range(100)])

ans.append([ '.' for _ in range(100)])

for i in range(1, 49):
    temp = [ '.' for _ in range(100)]
    if b > 0:
        if i % 2 != 0:
            for j in range(min(b, 49)):
                temp[2 * j + 1] = '#'
                b -= 1
        else:
            ans.append(temp)
            continue
    else:
        break
    ans.append(temp)

ans.append([ '.' for _ in range(100)])

print(len(ans), '100')

for x in ans:
    print(''.join(x))