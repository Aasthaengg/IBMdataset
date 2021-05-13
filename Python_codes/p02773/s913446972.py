import collections

N = int(input())
S = [input() for _ in range(N)]

cnt = collections.Counter(S)
max_cnt = max(cnt.values())

ans_list = []

for key, value in cnt.items():
    if value == max_cnt:
        ans_list.append(key)

print(*sorted(ans_list), sep='\n')

