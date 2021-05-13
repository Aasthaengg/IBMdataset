n, k, c = list(map(int, input().split()))
s = input()

mae, usiro = [-1] * n, [-1] * n

now, at = 1, 0
while at < n:
    if s[at] == 'x':
        at += 1
    else:
        mae[at] = now
        at += c + 1
        now += 1
        if now > k:
            break

now, at = k, n-1
while at >= 0:
    if s[at] == 'x':
        at -= 1
    else:
        usiro[at] = now
        at -= c + 1
        now -= 1
        if now <= 0:
            break

for i in range(n):
    if mae[i] != -1 and mae[i] == usiro[i]:
        print(i + 1)
