h, w = map(int, input().split())

lis = [list(input().split()) for _ in range(h)]

for i in lis:
    for _ in range(2):
        for j in i:
            print(j)