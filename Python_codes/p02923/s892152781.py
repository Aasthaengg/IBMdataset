n = int(input())
H = list(map(int, input().split()))

piv = 1
pre_ans = 0
pre_h = H[0]
ans = 0
while piv < n:
  if H[piv] <= pre_h:
    pre_h = H[piv]
    piv += 1
    pre_ans += 1
  else:
    ans = max(ans, pre_ans)
    pre_h = H[piv]
    piv += 1
    pre_ans = 0
  #print(pre_ans)
ans = max(ans, pre_ans)
print(ans)