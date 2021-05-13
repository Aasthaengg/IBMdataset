h, w = map(int, input().split())
c = [list(map(str, input().split())) for _ in range(h)]

for i in range(h):
    x = c[i]
    print(''.join(x))
    print(''.join(x))