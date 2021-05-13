X, Y, Z, K = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))[::-1]

A_B = []
for a in A:
    for b in B:
        A_B.append(a + b)

A_B = sorted(A_B)

def bin_search(mid):
    res = 0
    idx = 0
    ans = [] 
    for c in C:
        while idx < len(A_B):
            if c + A_B[idx] >= mid:
                res += len(A_B) - idx
                ans.append((c, idx))
                break
            else:
                idx += 1

    return res, ans

ok = 0
ng = pow(10, 10) * 3 + 1

while ok + 1 < ng:
    mid = (ok + ng) // 2
    res, ans = bin_search(mid)
    if res >= K:
        ok = mid
    else:
        ng = mid

res, ans = bin_search(ok)

tmp_ans = []
for c, idx in ans:
    for i in range(idx, len(A_B)):
        tmp_ans.append(A_B[i] + c)
for ans in sorted(tmp_ans)[::-1][:K]:
    print(ans)