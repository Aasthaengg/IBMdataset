N = int(input())
A = [int(input()) for _ in range(N)]
sortA = sorted(A)
ma = sortA[-1]
ma2 = sortA[-2]
for a in A:
    if a == ma:
        print(ma2)
    else:
        print(ma)
