from itertools import accumulate

N = int(input())
A = [int(input()) for _ in range(N)]

if A[0] != 0:
    print(-1)
else:
    A.reverse()
    bef = A[0]
    c = 0
    ans = 0
    for i in A:
        if bef!=i:
            if bef-i > 1:
                print(-1)
                break
            ans += bef*c
            c = 1 if bef<i else 0
        else:
            c += 1
        bef = i
    else:
        print(ans)
