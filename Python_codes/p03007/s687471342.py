
N = int(input())
X = list(map(int, input().split()))

pos = sorted([v for v in X if v >= 0])
neg = sorted([v for v in X if v < 0], reverse=True)

ans = []
if not neg:
    # neg is empty
    cnt = pos[0]
    for v in pos[1:-1]:
        ans.append((cnt, v))
        cnt -= v
    ans.append((pos[-1], cnt))
    print(pos[-1] - cnt)
elif not pos:
    # pos is empty
    cnt = neg[0]
    for v in neg[1:]:
        ans.append((cnt, v))
        cnt -= v
    print(cnt)
else:
    # neg and pos exist
    for v in pos[:-1]:
        ans.append((neg[0], v))
        neg[0] -= v

    cnt = pos[-1]
    for v in neg:
        ans.append((cnt, v))
        cnt -= v
    print(cnt)

for v in ans:
    print(*v)
