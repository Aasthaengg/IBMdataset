n = int(input())
for i in range(n, 1000):
    l = list(str(i))
    s = set(l)
    if len(s) == 1:
        print(i)
        exit()
