N, x = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

if x == sum(A):
    print(N)
else:
    A.sort()
    ans = 0
    for a in A[:-1]:
        if x >= a:
            ans += 1
            x -= a
        else:
            break
    print(ans)
