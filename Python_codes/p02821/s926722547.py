N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

AS = [0] * (N+1)
for i in range(N):
    AS[i+1] = AS[i]+A[i]

# DBG = []

def find(power):
    cnt = 0
    sam = 0
    for a in A:
        left = -1
        right = N
        while right-left>1:
            mid = left + (right-left)//2
            if a+A[mid] >= power:
                right = mid
            else:
                left = mid
        cnt += (N-right)
        sam += (AS[N]-AS[right]) + (N-right)*a
        # for i in range(right, N):
        #     DBG.append((A[i], a))
    return cnt, sam

left = 0
right = 10**15
while right-left>1:
    mid = left + (right-left)//2
    cnt, sam = find(mid)
    if cnt>M:
        left = mid
    else:
        right = mid

# ap+aq<=leftを満たすものの和を求める
cnt, ans = find(left)
print(ans - (cnt-M)*left)
