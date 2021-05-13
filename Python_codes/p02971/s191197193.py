N = int(input())
A = [next(map(int, input().split())) for _ in range(N)]

AA = sorted(A, reverse=True)

for i in A:
    if i != AA[0]:
        print(AA[0])
    else:
        print(AA[1])

