n, k = map(int, input().split())
s = input()

nums = []
now = 1 # 今見ている値
cnt = 0 # 今見ている値の連続する個数
for i in range(n):
    if s[i] == str(now): # 今見ているもの同じ場合
        cnt += 1
    else:
        nums.append(cnt)
        now ^= 1
        cnt = 1
# 最後の部分を追加
nums.append(cnt)
# 配列の大きさが奇数でないなら，0を追加
if len(nums) % 2 == 0:
    nums.append(0)

# 尺取法
left, right = 0, 0
tmp = 0 # [left, right)の総和

res = 0
for i in range(0, len(nums), 2): # 1のところを見ていく
    nextleft, nextright = i, min(i + 2 * k + 1, len(nums))
    while nextleft > left:
        tmp -= nums[left]
        left += 1
    while nextright > right:
        tmp += nums[right]
        right += 1
    res = max(res, tmp)
    
print(res)