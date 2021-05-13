import itertools

N = int(input())
count = [0, 0, 0, 0, 0]
for _ in range(N):
    l = input()[0]
    if l == 'M':
        count[0] += 1
    elif l == 'A':
        count[1] += 1
    elif l == 'R':
        count[2] += 1
    elif l == 'C':
        count[3] += 1
    elif l == 'H':
        count[4] += 1
ans = 0
for c in itertools.combinations(count, 3):
    ans += c[0]*c[1]*c[2]

print(ans)
