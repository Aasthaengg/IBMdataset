s = reversed(input())
# Bの右にあるWの総数を数える
ans = 0
cnt = 0
for x in s:
    if x=='W':
        cnt += 1
    else:
        ans += cnt

print(ans)