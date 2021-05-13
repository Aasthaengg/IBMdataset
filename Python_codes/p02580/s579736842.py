from itertools import product

def zero_origin(s: str) -> int:
  return int(s) - 1

H, W, M = map(int, input().split())
h_obj = [0 for _ in range(H)]
w_obj = [0 for _ in range(W)]
obj = set()
for _ in range(M):
  h, w = map(zero_origin, input().split())
  h_obj[h] += 1
  w_obj[w] += 1
  obj.add((h, w))
max_h = max(h_obj)
max_w = max(w_obj)
h_list = [h for h in range(H) if h_obj[h] == max_h]
w_list = [w for w in range(W) if w_obj[w] == max_w]
for h, w in product(h_list, w_list):
  if (h, w) not in obj:
    print(max_h + max_w)
    break
else:
  print(max_h + max_w - 1)