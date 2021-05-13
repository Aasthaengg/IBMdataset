N = int(input())
A = [int(input())for _ in range(N)]
ra = sorted(A,reverse = True)

for i in A:
    if i != ra[0]:
        print(ra[0])
    else:
        print(ra[1])