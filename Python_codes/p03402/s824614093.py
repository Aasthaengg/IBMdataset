A, B = map(int, input().split())
ans = [['.']*50 + ['#']*50 for i in range(500)]
cnt = 1
for i in range(0, 100, 2):
    for j in range(0, 49, 2):
        if cnt == B:
            break
        ans[i][j] = '#'
        cnt += 1
    if cnt == B:
        break
cnt = 1
for i in range(0, 100, 2):
    for j in range(51, 100, 2):
        if cnt == A:
            break
        ans[i][j] = '.'
        cnt += 1
    if cnt == A:
        break

print(100, 100)
for i in range(100):
    print(''.join(ans[i]))
