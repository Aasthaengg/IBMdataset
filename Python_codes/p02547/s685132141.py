n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

c = 0
ans = False
for i in d:
    if i[0] == i[1]:

        c += 1
        if c >=3:
            ans = True
            break
    else:
        c = 0
if ans:
    print('Yes')
else:
    print("No")