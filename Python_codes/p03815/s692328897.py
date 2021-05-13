x = int(input())

cnt = x // 11
mod = x % 11
cnt *= 2
if 0 < mod <= 6:
   cnt += 1
elif mod > 6:
   cnt += 2
print(cnt)
