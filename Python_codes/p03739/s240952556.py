n = int(input())
a = [int(x) for x in input().split()]
key = 0
ans = 0
for i in range(n):
  sub = key + a[i]
  if i == 0 and sub == 0:
    ans += 1
    sub = 1
  if i != 0 and sub*key >= 0:
    if key > 0:
      ans += sub+1
      sub = -1
    else:
      ans += 1-sub
      sub = 1
  key = sub

ans2 = 0
key2 = 0
for i in range(n):
  sub = key2 + a[i]
  if i == 0:
    if sub == 0:
      ans2 += 1
      sub = -1
    elif sub > 0:
      ans2 += sub+1
      sub = -1
    else:
      ans2 += 1-sub
      sub = 1
  if i != 0 and sub*key2 >= 0:
    if key2 > 0:
      ans2 += sub+1
      sub = -1
    else:
      ans2 += 1-sub
      sub = 1
  key2 = sub
      
print(min([ans, ans2]))