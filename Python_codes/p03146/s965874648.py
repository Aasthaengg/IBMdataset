s = int(input())
cnt = 1
a = []
ans = s
while not ans in a:
    a.append(ans)
    if ans % 2 == 0:
        ans /= 2
    else:
        ans = 3 * ans + 1
    cnt += 1
print(cnt)
