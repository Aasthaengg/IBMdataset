n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

lastans = -1e20

for i in range(n):
    now = p[i] - 1 
    score = [c[now]]
    while True:
        now = p[now] - 1
        score.append(score[-1] + c[now])
        if now == i:
            break
    loopsum = score[-1]
    looplen = len(score)
#    print(score)
    if looplen >= k:
        ans = max(score[:k])
    elif loopsum <= 0:
        ans = max(score)
    else:
        loopnum = k//looplen
        loopnum_mod = k % looplen
        ans1 = loopsum * (loopnum - 1) + max(score)
        ans2 = loopsum * loopnum
        if loopnum_mod != 0:
            ans2 = ans2 +max(0,max(score[:loopnum_mod]))
        ans =max(ans1,ans2)
    lastans = max(lastans,ans)

print(lastans)

