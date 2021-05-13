def solve(N, K, cards):
  min_elem = cards[0]

  # dp[i] == True: Current player will win if i stones left
  dp = [False for _ in range(K + 1)]
  for i in range(min_elem):
    dp[i] = False

  for k in range(1, K + 1):
    for c in cards:
      if c > k:
        break
      if k - c >= 0 and dp[k - c] == False:
        dp[k] = True

  print("First" if dp[K] else "Second")

  
def iln(): return list(map(int, input().split()))


N, K = iln()
cards = iln()
solve(N, K, cards)
