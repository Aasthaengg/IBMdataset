s = input()
s_start = 0
s_end = 0
count = 0

# 文字列sを右から探索できるように逆順に変換する
s_reverse = s[::-1]
# print(s_reverse)

for i in s:
    if i == 'A':
        s_start = count
        break
    count += 1

# カウンタcountを逆順用に変更（降順）
count = len(s) - 1

for j in s_reverse:
    if j == 'Z':
        s_end = count
        break
    count -= 1

ans = s_end - s_start + 1
print(ans)
