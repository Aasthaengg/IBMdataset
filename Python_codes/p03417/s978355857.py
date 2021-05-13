N, M = map(int, input().split())

min_NM = min(N,M)
max_NM = max(N,M)

if min_NM == 1 and max_NM == 1:
    print(1)
elif min_NM == 1:
    print(max_NM-2)
else:
    if min_NM == 2:
        print(0)
    else:
        ans = (N-2)*(M-2)
        print(ans)
