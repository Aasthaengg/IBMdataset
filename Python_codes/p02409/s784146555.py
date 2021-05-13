buildings =  [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())

    buildings[b-1][f-1][r-1] += v
sep = 1
for b in buildings:
    for f in b:
        print(" ",end="")
        print(*f)
    if sep != len(buildings):
        print("#" * 20)
        sep +=1

