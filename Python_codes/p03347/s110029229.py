import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

if A[0] != 0:
    ans = -1
else:
    for a, b in zip(A, A[1:]):
        if a == b:
            continue
        elif a > b:
            continue
        elif a+1 == b:
            continue
        else:
            ans = -1
            print(ans)
            exit()

    subA = []
    prev = -1
    l = 0
    tmp_array = []
    while l < N:
        if A[l] > prev:
            tmp_array.append(A[l])
            prev = A[l]
        else:
            prev = A[l]
            subA.append(tmp_array)
            tmp_array = [prev]

        l += 1
    subA.append(tmp_array)
    ans = sum([max(l) for l in subA])
print(ans)
