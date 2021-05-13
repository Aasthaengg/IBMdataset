h, w = map(int, input().split())
c = [input() for _ in range(h)]
for i in range(2*h):
    print(c[i//2])