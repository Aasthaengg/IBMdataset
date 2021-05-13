from itertools import accumulate

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse = True)
#print(A)

ok = -1
ng = 10 ** 11
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    left, right = 0, N - 1
    cnt = 0
    while left <= N - 1 and right >= 0:
        if A[left] + A[right] >= mid:
            cnt += right + 1
            left += 1
        else:
            if right:
                right -= 1
            else:
                left += 1
    if cnt >= M:
        ok = mid
    else:
        ng = mid
#print(ok)

Acum = [0] + list(accumulate(A))
#print(Acum)

left, right = 0, N - 1
cnt = 0
answer = 0
while left <= N - 1 and right >= 0:
    if A[left] + A[right] >= ok:
        cnt += right + 1
        answer += (right + 1) * A[left] + Acum[right + 1]
        left += 1
    else:
        if right:
            right -= 1
        else:
            left += 1
        
answer -= (cnt - M) * ok
print(answer)