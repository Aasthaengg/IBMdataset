a, b, c = map(int, input().split())
for i in [a, b, c]:
    if [a, b, c].count(i) == 1:
        print(i)
        exit()
