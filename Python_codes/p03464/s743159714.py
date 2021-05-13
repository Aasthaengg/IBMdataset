



K = int(input())
A = list(map(int, input().split()))

if A[-1] > 2:
    print(-1)
    exit()



hi = 2
lo = 2

for i in reversed(range(K)):



    new_hi = hi // A[i] * A[i] + (A[i] - 1)

    if lo // A[i] > 0 and lo % A[i] > 0:
        new_lo = (lo // A[i] + 1) * A[i]
    elif lo // A[i] > 0 and lo % A[i] == 0:
        new_lo = lo
    elif lo // A[i] == 0:
        new_lo = A[i]

    if new_hi < hi or new_lo < lo or new_hi < new_lo:
        print(-1)
        exit()


    

    hi = new_hi
    lo = new_lo


print(lo, hi)