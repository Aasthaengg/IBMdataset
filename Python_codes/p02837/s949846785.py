N = int(input())
A = []
for i in range(N):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        A.append((i, x-1, y))

ans = 0
for i in range(2 ** N):
    for (j,x,y) in A:
        if i & 1 << j:
            if y == 1:
                if not i & (1 << x):
                    break
            else:
                if i & (1 << x):
                    break
    else:
        ans = max(ans, sum([1 for x in bin(i) if x == '1']))
print(ans)
