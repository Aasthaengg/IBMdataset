n = int(input())
A = tuple(map(int, input().split()))
ma = min(A)
while True:
    ra = set([a%ma for a in A if a%ma > 0])
    if len(ra) == 0:
        print(ma)
        break
    minra = min(ra)
    if ma == minra:
        print(ma)
        break
    ma = minra
