N = int(input())
P = list(map(int, input().split()))
cnt = sum([(x - i) != 0 for i, x in enumerate(P, 1)])
if cnt == 0 or cnt == 2:
    print('YES')
else:
    print('NO')