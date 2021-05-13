N,K = map(int,input().split())
A = [int(x) for x in input().split()]
F = [int(x) for x in input().split()]
A.sort()
F.sort(reverse=True)
AF =  [A[i]*F[i] for i in range(N)]
maxAF = max(AF)
#二分探索
ans = maxAF
left = 0
right = maxAF
while True:
    mid = (left + right)//2
    dis = 0
    syugyo = 0
    for i in range(N):
        af = AF[i]
        if af > mid:
            dis += af-mid
            amari = (af-mid)%F[i]
            count = (af-mid)//F[i]
            if amari == 0:
                syugyo += count
            else:
                syugyo += count +1
    if syugyo > K:
        if right-mid == 1:
            ans = right
            break
        else:
             left = mid
    else:
        if mid-left == 1:
            ans = mid
            break
        else:
            right = mid
if sum(A) <= K:
    ans = 0
print(ans)