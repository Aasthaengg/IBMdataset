def check_load(k, w, max_weight) -> bool:
  truck_itr = 0
  truck_weight = 0
  for w_i in w:
    if w_i > max_weight:
      return False
    if truck_weight + w_i > max_weight:
      truck_weight = 0
      truck_itr += 1

    truck_weight += w_i
    if truck_itr > k-1:
      return False
    
  return True

def solve():
  # input
  n,k = map(int, input().split())
  w = []
  truck = []
  for i in range(1,n+1):
    w.append(int(input()))

  # kの積載量に対してトラックに詰めこむ操作の二分法で探索する。
  right = sum(w) # 解の上界
  left = sum(w)//n # 平均を床関数とったものが下界
  max_weight = left
  while right-left > 1:
    # print(left,right,max_weight)
    if check_load(k, w, max_weight):
      right = max_weight
    else:
      left = max_weight

    max_weight = (right+left)//2
  
  print(right)
  
solve()
