import collections

N = int(input())
S = [input() for _ in range(N)]
S.sort()
#print(S)
ans = collections.Counter(S)
values, cnt = zip(*ans.most_common())
#print(values)
#print(cnt)
max_count = cnt[0]
for i in range(len(cnt)):
    if max_count > cnt[i]:
        break
    print(values[i])