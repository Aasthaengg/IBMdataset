import collections

N = int(input())
cnt_dic = collections.defaultdict(int)

for _ in range(N):
  s = input()
  cnt_dic[s] += 1

max_v = max(cnt_dic.values())

ans_lis = [k for k, v in cnt_dic.items() if v == max_v]

for s in sorted(ans_lis):
  print(s)
