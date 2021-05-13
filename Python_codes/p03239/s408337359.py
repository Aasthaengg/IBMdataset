def resolve():
    N, T = list(map(int, input().split()))
    CT = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    for cost, time in CT:
        if time > T:
            continue
        print(cost)
        break
    else:
        print("TLE")



if '__main__' == __name__:
    resolve()