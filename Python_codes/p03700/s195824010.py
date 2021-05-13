N, A, B = [int(i) for i in input().split()]
Hn = [int(input()) for _ in range(N)]
dAB = A - B

def check(X):
  base = B * X
  counts = sum([max((h - base + dAB - 1)//dAB, 0) for h in Hn])
  return counts <= X
               
def min_binary_search(check, l=0, r=100000000000):
    while r - l > 1:
      mid = (l + r) // 2
      if check(mid):
        r = mid
      else:
        l = mid
    return r
print(min_binary_search(check))