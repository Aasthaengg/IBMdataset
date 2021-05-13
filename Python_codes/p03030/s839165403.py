def resolve():
    N = int(input())
    city = []
    for i in range(N):
        s, p = input().split()
        city.append([s, int(p), i+1])
    city.sort(key = lambda city : (city[0], -city[1]))
    for j in range(N):
        print(city[j][2])
resolve()