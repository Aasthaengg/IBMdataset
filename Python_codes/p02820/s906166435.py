n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

point = 0
for i in range(n):
    if (i >= k) & (t[i] == t[i - k]):
        t[i] = 'a'
        continue
    else:
        if t[i] == 'r':
            point += p
        elif t[i] == 's':
            point += r
        else:
            point += s
print(point)