a = input()
len_a = len(a)
cnt = [0] * 26
for i in a:
  cnt[ord(i)-ord("a")] += 1
ans = len_a * (len_a-1) // 2 + 1
for i in cnt:
  ans -= i * (i-1) // 2
print(ans)