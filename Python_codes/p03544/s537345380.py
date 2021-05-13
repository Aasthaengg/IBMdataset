def resolve():
    n = int(input())
    lli = [2, 1]
    if n <= 1:
        print(lli[n])
    else:
        for i in range(2, n+1):
            lli.append(lli[i-1] + lli[i-2])
        print(lli[n])
resolve()