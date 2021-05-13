from collections import Counter
n = int(input())
lst = list(map(int, input().split()))
mclst = Counter(lst).most_common()
sqlst = []
rclst = []
for tpl in mclst:
  if tpl[1] >= 2:
    rclst.append(tpl[0])
  if tpl[1] >= 4:
    sqlst.append(tpl[0])
sqmax, rcmax = 0, 0
if len(sqlst) >= 1:
  sqmax = max(sqlst) ** 2
if len(rclst) >= 2:
  rclst.sort(reverse=True)
  rcmax = rclst[0] * rclst[1]
print(max(sqmax, rcmax))