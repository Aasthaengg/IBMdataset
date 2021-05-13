s = input()

ls = [0 for _ in range(len(s))]

i = 0
cnt = 0
now = 'R'
while True:
    if s[i] == now:
        cnt += 1
        i += 1
    if i == len(s) or s[i] != now:
        if now == 'R':
            ls[i] += cnt // 2
            if cnt % 2 == 0:
                ls[i-1] += cnt // 2
            else:
                ls[i-1] += cnt // 2 + 1
            now = 'L'
        else:
            ls[i-cnt-1] += cnt // 2
            if cnt % 2 == 0:
                ls[i-cnt] += cnt // 2
            else:
                ls[i-cnt] += cnt // 2 + 1
            now = 'R'

        cnt = 0
    if i == len(s):
        break

print(' '.join(map(str, ls)))

