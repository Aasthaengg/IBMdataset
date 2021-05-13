n = int(input())
i = 1
cnt = 0
while cnt < n:
    cnt += i
    i += 1

for j in range(1, i):
    if cnt - n == j:
        continue
    print(j)
