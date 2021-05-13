def solve():
  k, a, b = map(int, input().split())

  # 交換しても得しない、地道に増やす
  if b - a <= 2: return 1 + k

  # 交換できる数まで増えずに終了 (終了2回前にa個に到達していること)
  if 1 + (k - 2) < a: return 1 + k

  # 交換できる数まで増えたら、交換し続ける
  # 最初1個あるので a-1 回で最初の交換可能へ到達
  # k-(a-1)//2 回は交換できて、毎回 b-a が増える
  exchange_times, last = divmod(k-(a-1), 2)
  profit = b - a
  ans = a + exchange_times * profit + last
  return ans

ans = solve()
print(ans)