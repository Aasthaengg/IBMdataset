n = int(input())
lst = list(map(int, input().split()))
hlst = [0]
for h in lst:
  if hlst[-1] != h:
    hlst.append(h)
hlst.append(0)
ans = 0
l = len(hlst)
for i in range(1, l - 1):
  if hlst[i - 1] < hlst[i] and hlst[i] > hlst[i + 1]:
    ans += hlst[i]
  elif hlst[i - 1] > hlst[i] and hlst[i] < hlst[i + 1]:
    ans -= hlst[i]
print(ans)