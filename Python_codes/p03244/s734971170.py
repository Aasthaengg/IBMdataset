from collections import defaultdict
n = int(input())
v = list(map(int, input().split()))
o = defaultdict(int)
e = defaultdict(int)
odd_num = 0
even_num = 0
for i, v_one in enumerate(v):
  if i % 2 == 1:
    o[v_one] += 1
    odd_num += 1
  else:
    e[v_one] += 1
    even_num += 1
sorted_o = sorted(o.items(), key=lambda x:-x[1])
sorted_e = sorted(e.items(), key=lambda x:-x[1])
if sorted_o[0][0] != sorted_e[0][0]:
  ans = odd_num - sorted_o[0][1] + even_num - sorted_e[0][1]
elif len(sorted_o) >= 2 and len(sorted_e) >= 2:
  ans1 = odd_num - sorted_o[1][1] + even_num - sorted_e[0][1]
  ans2 = odd_num - sorted_o[0][1] + even_num - sorted_e[1][1]
  ans = min(ans1, ans2)
elif len(sorted_o) >= 2:
  ans = sorted_o[0][1]
elif len(sorted_e) >=2:
  ans = sorted_e[0][1]
else:
  ans = odd_num
print(ans)