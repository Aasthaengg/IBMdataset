N = int(input())
ppp = list(map(int, input().split()))
cnt = 0
for i, p in enumerate(ppp, 1):
    if i != p:
        cnt += 1
print('YES' if cnt < 3 else 'NO')
