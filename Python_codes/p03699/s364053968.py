N, *S = map(int, open(0).read().split())
sum_S = sum(S)
if sum_S % 10:
    print(sum_S)
else:
    ans = 0
    for s in S:
        score = sum_S - s
        if score % 10 == 0:
            continue
        ans = max(ans, score)
    print(ans)
