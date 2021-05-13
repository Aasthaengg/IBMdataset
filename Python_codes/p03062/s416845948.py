N = int(input())
A = list(map(int, input().split()))

cnt = len([a for a in A if a < 0])
if cnt % 2 == 0:
    print(sum([abs(a) for a in A]))
else:
    ans = sum([abs(a) for a in A])
    M = float('inf')
    for a in A:
        if abs(a) < M:
            M = abs(a)
    print(ans - 2 * M)
