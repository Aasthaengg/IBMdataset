def abc131d_megalomania():
    n = int(input())
    d = []
    for _ in range(n):
        d.append(list(map(int, input().split())))
    d.sort(key=lambda x: x[1])
    t = 0
    for item in d:
        t += item[0]
        if t > item[1]:
            print('No')
            return
    print('Yes')
abc131d_megalomania()