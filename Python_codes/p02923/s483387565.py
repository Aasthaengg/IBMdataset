N = int(input())
H = list(map(int, input().split()))
base = H[-1]
cnt = 0
ans = 0
if N == 1:
    print(0)
else:
    for h in H[N-2::-1]:
        if base <= h:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
        base = h
    print(max(ans,cnt))