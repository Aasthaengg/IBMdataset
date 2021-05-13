# E - Multiplication 4
import heapq
N, K = map(int, input().split())
A = list(int(a) for a in input().split())
MOD = 10**9 + 7

# N = K の時
if N == K:
    ans = 1
    for a in A:
        ans = (ans * a) % MOD

else:
    pos = []
    neg = []
    for a in A:
        if a >= 0:
            pos.append(a)
        else:
            neg.append(a)

    # 必ずマイナスになる時＝全てがマイナスの値であり、
    # かつKが奇数の時
    if len(neg) == N and K&1 == 1:
        neg.sort(reverse=True)
        ans = 1
        for i in range(K):
            ans = (ans * neg[i]) % MOD

    # それ以外のプラスになるケース
    # プラスの要素とマイナスの要素を絶対値の大きい順にソートし、
    # Kが奇数であれば、プラスのリストから1つ選び、
    # 残りの偶数個のKに対して、２つずつを選んだ時の
    # 大きい方から取得していく
    else:
        pos.sort(reverse=True)
        pos2 = []
        ans = 1
        ini = 0
        rem = K
        if K&1 == 1:
            ans = (ans * pos[0]) % MOD
            ini = 1
            rem -= 1
        for i in range(0, (len(pos)-ini)//2):
            heapq.heappush(pos2, (pos[i*2+ini] * pos[i*2+ini+1])*-1)
        neg.sort()
        neg2 = []
        for i in range(0, len(neg)//2):
            heapq.heappush(neg2, (neg[i*2] * neg[i*2+1]) * -1)
        while rem > 0:
            if (pos2 != [] and neg2 == []) or (pos2 != [] and neg2 != [] and pos2[0] <= neg2[0]):
                tmp = heapq.heappop(pos2) * -1
            else:
                tmp = heapq.heappop(neg2) * -1
            ans = (ans * tmp) % MOD
            rem -= 2

print(ans)