s = input()

l = len(s)

point = 0
cnt = 0
for i in s:
    if cnt > 0:
        cnt -= 1
        if i == 'g':
            point += 1
    else:
        cnt += 1
        if i == 'p':
            point -= 1
print(point)
