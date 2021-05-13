def resolve():
    N = int(input())
    lic = [2, 1]
    for i in range(85):
        lic.append(lic[-1]+lic[-2])
    print(lic[N])
resolve()