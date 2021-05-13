S = input()

cnt = {'a': 0, 'b': 0, 'c': 0}
for s in S:
    cnt[s] += 1

cnt_list = [[v, k] for k, v in cnt.items()]
cnt_list.sort(reverse=True)

if len(S) == 1:
    print("YES")
    exit(0)

if len(S) == 2:
    v, k = cnt_list[0]
    if v == 2:
        print("NO")
    else:
        print("YES")
    exit(0)

_, prev2 = cnt_list[0]
_, prev1 = cnt_list[1]
cnt[prev2] -= 1
cnt[prev1] -= 1
for i in range(2, len(S)):
    curr = 'a'
    for c in ('a', 'b', 'c'):
        if c != prev2 and c != prev1:
            curr = c
    if cnt[curr] > 0:
        cnt[curr] -= 1
        prev2 = prev1
        prev1 = curr
    else:
        print("NO")
        exit(0)

print("YES")
