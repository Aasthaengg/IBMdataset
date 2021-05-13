def resolve():
    import itertools
    import math
    def distance(i, j):
        return math.sqrt((i[0]-j[0])**2+(i[1]-j[1])**2)

    n = int(input())
    l = list(range(n))
    X_Y = []
    for i in range(n):
        X_Y.append(list(map(int, input().split())))
    p_list = list(itertools.permutations(l, n))
    total = 0
    for p in p_list:
        p_t = 0
        for index in range(n-1):
            p_t += distance(X_Y[p[index]], X_Y[p[index+1]])
        total += p_t
    print(total/len(p_list))
resolve()