h, w = map(int, input().split())
cl = [ input() for _ in range(h)]

for i in range(2*h):
    if i%2 == 0:
        print(cl[i//2])
    else:
        print(cl[(i-1)//2])
