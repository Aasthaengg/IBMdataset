m, k = map(int, input().split())

n = 2 ** m

if k >= n:
    print(-1)
    exit()

if m == 0:
    print('0 0')
    exit()
elif m == 1:
    if k == 0:
        print('0 0 1 1')
    else:
        print(-1)
    exit()

ans = []
for i in range(n):
    if i == k:
        continue
    ans.append(i)

ans.append(k)

for i in range(n-1, -1, -1):
    if i == k:
        continue
    ans.append(i)

ans.append(k)

print(' '.join(map(str, ans)))