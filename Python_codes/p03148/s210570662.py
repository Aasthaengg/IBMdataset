# 最大価値が取れて種類数も増えるなら必ずとる
# 
# 種類数を固定すると：各種類のベストを見て貪欲に種類を決めているはず
# あとは種類数を更新できないものの中から貪欲
#
# 最大価値が等しい2種類：第2種の貪欲が使われだすなら両方取ってるはずなので優先度は同じでよい
#
# 種類数を増やしたときの変化を見る

import sys
input = sys.stdin.readline
from heapq import heappush,heappop

N,K = map(int,input().split())
kind_value = [[] for _ in range(N+1)]
for _ in range(N):
  t,d = map(int,input().split())
  kind_value[t].append(d)
for li in kind_value:
  li.sort()
  
first_type = [(li[-1],i) for i,li in enumerate(kind_value) if li]
first_type.sort(reverse = True)

kind = 0
value_type1 = 0
second_type = []
second_type_sum = 0
second_type_cnt = 0

answer = 0
for v,i in first_type:
  kind += 1
  if kind > K:
    break
  value_type1 += v
  for d in kind_value[i][:-1]:
    heappush(second_type,d)
    second_type_sum += d
    second_type_cnt += 1
  while second_type_cnt > K-kind:
    d = heappop(second_type)
    second_type_cnt -= 1
    second_type_sum -= d
  value = kind*kind + value_type1 + second_type_sum
  if answer < value:
    answer = value

print(answer)
