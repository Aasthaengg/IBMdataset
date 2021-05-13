n = int(input())
a = list(map(int, input().split()))

def solve(a, n, bool):  # bool = True: 偶数項を足した時に正
  change = 0
  sum = 0
  for i in range(n):
    sum+=a[i]
    if sum <= 0 and bool:  # 和が正を仮定しているのに0以下なら
      change += abs(1-sum)
      sum=1
    if sum >=0 and not bool:
      change += abs(-1-sum)
      sum=-1 
    bool = not bool
  return change

print(min(solve(a,n,True),solve(a,n,False)))