n = int(input())
S = [int(input()) for _ in range(n)]
t = [s for s in S if s % 10 != 0]
if len(t) == 0:
    print(0)
    exit()
ans = sum(S)
if ans % 10 == 0:
    print(ans - min(t))
else:
    print(ans)
