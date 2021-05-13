n, c, k = list(map(int, input().split()))
t = []

for i in range(n):
    t.append(int(input()))

t = sorted(t)

cnt = 1
cap = 1
first = t[0]

for i in range(1, n):
    if t[i] > first + k:
        cnt += 1
        cap = 1
        first = t[i]
    elif cap == c:
        cnt += 1
        cap = 1
        first = t[i]
    else:
        cap += 1

print(cnt)