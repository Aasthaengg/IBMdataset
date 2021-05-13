s = str(input())
k = int(input())

cnt = 0
for i in range(len(s)):
    if s[i] == '1':
        cnt += 1
    else:
        c = s[i]
        break

if cnt:
    if cnt >= k:
        print('1')
    else:
        print(c)
else:
    print(c)
