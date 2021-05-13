def resolve():
    n = int(input())
    al = list(map(int, input().split()))
    al = sorted(al, reverse=True)
    an = 0
    bn = 0
    for i in range(n):
        if i % 2 == 0:
            an += al[i]
        elif i % 2 == 1:
            bn += al[i]
    print(an - bn)
resolve()