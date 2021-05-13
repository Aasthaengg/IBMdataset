def main():
    N, T = map(int, input().split())
    l = []
    cost = 1001
    for i in range(N):
        l.append(list(map(int, input().split())))
    for i in range(N):
        if l[i][1] <= T:
            t = l[i][1]
            if l[i][0] < cost:
                cost = l[i][0]
    if cost == 1001:
        print('TLE')
    else:
        print(cost)
main()  