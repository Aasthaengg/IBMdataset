n = int(input())
A = list(map(int,input().split()))[::-1]


def b():
    if A[0] != 2:
        return -1
    else:
        ans = [2, 3]
        for i in range(1, n):
            r = ans[1] // A[i] * A[i]
            l = -((-ans[0] // A[i]) * A[i])
            # print(-ans[0] // A[i])
            # print(l, r)
            if r < l:
                return -1
            ans = [l, r+A[i]-1]
            # print(ans)
    return ans

ans = b()
if ans == -1:
    print(ans)
else:
    print(ans[0], ans[1])