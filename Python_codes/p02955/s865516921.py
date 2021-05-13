def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sA = sum(A)
    divs = []
    i = 1
    while i * i < sA:
        if sA % i == 0:
            divs.append(i)
            divs.append(sA // i)
        i += 1
    if i * i == sA:
        divs.append(i)
    divs.sort()
    for d in reversed(divs):
        t = [i % d for i in A]
        t.sort()
        k = sum(t[:-sum(t) // d])
        if k <= K:
            return d

print(main())
