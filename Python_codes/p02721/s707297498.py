n, k, c = map(int, input().split())
s = input()

l = [-c-1]
for i in range(n):
    if s[i] == 'o' and i - l[-1] > c:
        l.append(i)
r = [n + c]
for i in reversed(range(n)):
    if s[i] == 'o' and r[-1] - i > c:
        r.append(i)
r.reverse()


if len(l)-1 == k:
    for li, ri in zip(l[1:], r):
        if li == ri:
            print(li + 1)