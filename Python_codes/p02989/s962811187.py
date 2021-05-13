def abc132c_divide_the_problem():
    n = int(input())
    d = sorted(list(map(int, input().split())))
    print(d[n // 2] - d[n // 2-1])
abc132c_divide_the_problem()