N = int(input())
S = []
for _ in range(N):
    S.append(int(input()))
S = sorted(S)

ans = sum(S)
if ans % 10 != 0:
    print(ans)
else:
    for s in S:
        if s % 10 != 0:
            print(ans - s)
            break
    else:
        print(0)