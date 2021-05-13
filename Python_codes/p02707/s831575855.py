from collections import Counter
N = int(input())
A = list(map(int, input().split()))
subordinates = [0] * N
boss_and_cnt = Counter(A)
for boss, cnt in boss_and_cnt.items():
  subordinates[boss - 1] = cnt
for s in subordinates:
  print(s)