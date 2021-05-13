n = int(input())
p = [int(x) for x in input().split()]

skip = False
cnt = 0
for i in range(n):
    if skip:
        skip = False
    elif p[i] == i + 1:
        cnt += 1
        skip = True
else:
    print(cnt)