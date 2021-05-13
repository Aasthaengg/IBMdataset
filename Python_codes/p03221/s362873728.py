def solve():
  N, M = map(int, input().split())
  A = [list(map(int, input().split()))+[i] for i in range(M)]

  A.sort(key=lambda x:(x[0],x[1]))
  ans = [0]*M
  before = -1
  for p,y,i in A:
    if p!=before:
      year = 1
    else:
      year += 1
    ans[i] = '0'*(6-len(str(p)))+str(p)+'0'*(6-len(str(year)))+str(year)
    before = p
  return ans
print(*solve(),sep='\n')