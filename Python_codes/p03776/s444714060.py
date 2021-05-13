N, A, B = map(int, input().split())

items = sorted(list(map(int, input().split())), reverse=True)

ans_lis = items[:A]
ans1 = sum(ans_lis)/A 
print(ans1)

i = A
ans2 = 0
while i <= B:
  if sum(items[:i])/i != ans1:
    break
  min_ = min(items[:i])
  min_in_ans = items[:i].count(min_)
  min_in_all = items.count(min_)

  nCr = {}
  def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

  ans2 += cmb(min_in_all, min_in_ans)
  i += 1
print(ans2)