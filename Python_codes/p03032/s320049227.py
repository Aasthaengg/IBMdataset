import sys

N, K = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))

ans = 0

for i in range(N+1):
    if K < i:
        continue
    score = sum(V[0:i])
    # print("i", i, "l score", score)
    ans = max(ans, score)
    for j in range(N+1):
        if N < i + j or K < i + j:
            continue
        tmp = score
        tmp += sum(V[N-j:])
        ans = max(ans, tmp)
        # print("i", i, "j", j, "lr score", tmp)

        # 捨てる最大個数
        k = K - i - j
        if k < 0:
            continue
        negs = []
        for n in range(0, i):
            if V[n] < 0:
                negs.append(V[n])
        for n in range(N-j, N):
            if V[n] < 0:
                negs.append(V[n])
        negs.sort()
        # print(negs)
        tmp -= sum(negs[:k])
        ans = max(ans, tmp)
        # print("i", i, "j", j, "k", k, "lrd score", tmp)

print(ans)