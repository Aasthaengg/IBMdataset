s = input()
N = len(s)

j = N-1
xi = 0
xj = 0
res = 0
for i in range(N):
    if s[i] == 'x':
        xi += 1
        continue
    while j>=i:
        if s[j] == 'x':
            xj += 1
            j -= 1
            continue

        if s[i] != s[j]:
            print(-1)
            exit()
        res += abs(xj-xi)
        j -= 1
        break
    xi = xj = 0
print(res)