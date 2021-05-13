import collections
MOD = 10**9+7

n = int(input())
a = [int(_) for _ in input().split()]

A = sorted(collections.Counter(a).most_common())

flg = True
ans = 1

if n % 2 == 0:
    # EVEN
    if len(A) == n//2:
        for i in range(n//2):
            if A[i][0] == 1+i*2 and A[i][1] == 2:
                ans = ans * 2 % MOD
            else:
                flg = False
                break
    else:
        flg = False
else:
    # ODD
    if len(A) == n//2+1:
        for i in range(n//2+1):
            if i == 0:
                if A[i][0] == 0 and A[i][1] == 1:
                    pass
                else:
                    flg = False
                    break
            else:
                if A[i][0] == i*2 and A[i][1] == 2:
                    ans = ans * 2 % MOD
                else:
                    flg = False
                    break
    else:
        flg = False

if flg:
    print(ans)
else:
    print(0)