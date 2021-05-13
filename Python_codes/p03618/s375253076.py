A = input()
_memo = {}
ans = 1
for i,a in enumerate(A):
  ans += i - _memo.setdefault(a,0)
  _memo[a] += 1
  #print(ans)
  #print(_memo)
print(ans)