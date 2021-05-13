n = int(input())
ans = 0
hoges = []
seeds = 'ATCG'
def ng(currents):
  v = 'AGC' in currents
  # for k in range(max(1, 0), len(currents)):
  for k in range(max(1, len(currents) - 3), len(currents)):
    v = v or 'AGC' in (currents[:k-1] + currents[k] + currents[k-1] + currents[k+1:])
  return v
memo = {}
ng_memo = {} # 後ろ4つだけ見ればNGわかる？
def f(index, currents):
  ng_key = currents[-4:]
  key = '%d:%s' % (index, currents[-4:])
  # print(key)
  if ng_key in ng_memo:
    return 0
  if key in memo:
    return memo[key]
  if ng(currents):
    ng_memo[key] = True
    return 0
  if index == n:
    return 1
  memo[key] = sum([f(index+1, currents + s) for s in seeds])
  return memo[key]

print(f(0, '') % int(1e9+7))

# 3:      61
# 4:     230
# 5:     865
# 6:    3247
# 7:   12185
# 8:   45719
