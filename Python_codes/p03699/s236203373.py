n = int(input())
S = [int(input()) for _ in range(n)]
S = [0] + sorted(S)
ss = sum(S)
for s in S:
    if (ss - s)%10 > 0:
        print(ss-s)
        break
else:
    print(0)
