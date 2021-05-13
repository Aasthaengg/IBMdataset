def all_pos(lst):
    for e in lst:
        if e < 0:
            return False
    return True

def all_neg(lst):
    for e in lst:
        if e > 0:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))

ans = []
M = 0
if all_pos(A):
    A.sort()
    res = A[0]
    for i in range(1, N - 1):
        ans.append((res, A[i]))
        res -= A[i]
    ans.append((A[-1], res))
    M = A[-1] - res
elif all_neg(A):
    A.sort()
    A.reverse()
    res = A[0]
    for i in range(1, N):
        ans.append((res, A[i]))
        res -= A[i]
    M = res
else:
    A.sort()
    A.reverse()
    tmp_neg = A[-1]
    tmp_pos = A[0]
    for i in range(1, len(A) - 1):
        if A[i] >= 0:
            ans.append((tmp_neg, A[i]))
            tmp_neg -= A[i]
        else:
            ans.append((tmp_pos, A[i]))
            tmp_pos -= A[i]
    ans.append((tmp_pos, tmp_neg))
    M = tmp_pos - tmp_neg
    
print(M)
for e in ans:
    print(e[0], e[1])