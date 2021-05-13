n = int(input())
s = [2]
ans = []
t = 1
for i in range(3,55556):
    flg = True
    for _ in s:
        if i % _ == 0:
            flg = False
    if flg:
        s.append(i)
        if i % 5 == 1:
            ans.append(str(i))
            t += 1
    if t > n:
        break
print(' '.join(ans))