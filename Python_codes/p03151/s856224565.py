n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# aの合計値がbの合計値を下回る場合は終了
total_a = sum(a)
total_b = sum(b)
if total_a < total_b:
  print(-1)
  exit()
  
# 数列aと数列bの差分を取得  
nums = [0]*n
for i in range(n): nums[i] = a[i] - b[i]
nums.sort()

ans = 0
m = 0
for i in range(n): # 差分がマイナスの値の合計と数を取得
  if nums[i] < 0:
    m += nums[i]
    ans += 1
  else: break

# 差分の大きい値から順にマイナス分を相殺していき、マイナスが終了した時点の変更数を回答する
for i in reversed(range(n)):
  if m >= 0:
    print(ans)
    break
  else:
    m += nums[i]
    ans += 1