a = sorted(map(int, input().split()), reverse=True)

diff1 = a[0] - a[1]
diff2 = a[0] - a[2]
cnt1 = diff1 // 2
cnt2 = diff2 // 2
result = sum([cnt1, cnt2])

diff1 -= cnt1 * 2
diff2 -= cnt2 * 2

s = sum([diff1, diff2])
if s & 1:
  print(result + 2)
else:
  print(result + s // 2)