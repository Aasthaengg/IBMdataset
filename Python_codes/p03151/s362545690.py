# 余剰と不足に分ける 余剰の多いやつから使って不足の多いやつに振る

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if sum(a) < sum(b):
    print(-1)
    exit()

surplus = []
lack = []
for i in range(n):
    if a[i] > b[i]:
        surplus.append(a[i] - b[i])
    elif a[i] < b[i]:
        # 同値は含まない
        lack.append(b[i] - a[i])
if len(lack) == 0:
    print(0)
    exit()

surplus = sorted(surplus, reverse=True)
lack = sorted(lack, reverse=True)

# print(surplus, lack)

right = 0
ans = 1
for left in range(len(surplus)):
    while right < len(lack) and surplus[left] - lack[right] >= 0:
        surplus[left] -= lack[right]
        ans += 1
        right += 1
    if right == len(lack):
        break
    # ここまではギリギリ条件を満たしている
    if right < len(lack):
        # 次にleftを使わなきゃいけない
        ans += 1
        # あまったぶんを回す
        lack[right] -= surplus[left]
print(ans),