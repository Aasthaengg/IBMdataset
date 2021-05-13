N = int(input())
C = []
tmp_b = -1
for _ in range(N):
  tmp_n = int(input())
  if tmp_n != tmp_b:
    C.append(tmp_n)
    tmp_b = tmp_n

SUM = 1
DP_dict = {}

for c in C:
  if c not in DP_dict.keys():
    DP_dict[c] = SUM
  else:
    SUM += DP_dict[c]
    DP_dict[c] = SUM

print(SUM % (10**9+7))