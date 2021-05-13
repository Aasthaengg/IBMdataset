A, B, C = map(int, input().split())
S = [A, B, C]
D = max(S)
less = [0, 0, 0]
for i in range(3):
  less[i] = D - S[i]
less = sorted(less)

ans = less[1]
remain = less[2] - less[1]
if remain % 2 == 0:
  ans += remain // 2
else:
  ans += (remain // 2) + 2

print(int(ans))
