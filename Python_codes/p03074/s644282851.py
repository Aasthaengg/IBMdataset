n, k = map(int, input().split())
s = input()

nums = []
now = 1 # 今見ている数
cnt = 0 # nowが並んでいる個数
for i in range(n):
    if s[i] == str(now):
        cnt += 1
    else:
        nums.append(cnt) # 切り替わりで追加
        now = 1 - now # 0と1を切り替える
        cnt = 1 # 新しいものをカウントし始める
# 最後
if cnt != 0:
    nums.append(cnt)

# 調整
if len(nums) % 2 == 0:
    nums.append(0)

add = 2 * k + 1

# 累積和を作る
acc = [0] * (len(nums) + 1)
for i in range(len(nums)):
    acc[i + 1] = acc[i] + nums[i]

res = 0
# 偶数番目だけ見る
for i in range(0, len(nums), 2):
    # [left, right)
    left = i
    right = min(i + add, len(nums))
    tmp = acc[right] - acc[left]
    res = max(res, tmp)

print(res)