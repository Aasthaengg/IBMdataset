n = int(input())
b = list(map(int, input().split()))

ans = []
while True:
    flag = False
    if len(b) == 0:
        break

    for i in range(len(b)):
        if i+1 == b[i]:
            idx = i
            flag = True
    if flag:
        tmp = b.pop(idx)
        ans.append(tmp)
    else:
        ans = [-1]
        break

print('\n'.join(map(str, reversed(ans))))
