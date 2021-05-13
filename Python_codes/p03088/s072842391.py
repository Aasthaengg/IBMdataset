n = int(input())
seeds = 'ATCG'
def ng(currents):
  v = 'AGC' in currents
  for k in range(max(1, len(currents) - 3), len(currents)):  # 先頭の方はチェック済み
    v = v or 'AGC' in (currents[:k-1] + currents[k] + currents[k-1] + currents[k+1:])[-4:]
  return v
 
memo = {}  # 今の長さと最新4つだけメモする
def f(index, currents):
  key = '%d:%s' % (index, currents[-4:])
  if key not in memo:
    if ng(currents):
      memo[key] = 0
    else:
      memo[key] = 1 if index == n else sum([f(index+1, currents + s) for s in seeds])
  return memo[key]
 
print(f(0, '') % int(1e9+7))