n = int(input())
p = []
for i in range(n):
    p.append(int(input()))

count = 0
if p[0] != 0:
    print(-1)
    exit()

for i in range(1, n):
    diff = p[i] - p[i - 1]
    if diff >= 2:
        print(-1)
        exit()
    elif diff == 1:
        count += 1
    else:
        count += p[i]

print(count)
