N = int(input())
ba = [list(map(int, input().split()[::-1])) for _ in range(N)]

ba.sort()
time = 0
for b, a in ba:
    time += a
    if b < time:
        print('No')
        exit()
print('Yes')