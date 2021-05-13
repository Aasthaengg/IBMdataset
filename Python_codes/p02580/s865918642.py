
h, w, m = map(int, input().split())

h_b_list = [0 for i in range(h)]
w_b_list = [0 for i in range(w)]

targets = set()
for i in range(m):
  bh, bw = map(int, input().split())
  targets.add((bh, bw))
  h_b_list[bh-1] += 1
  w_b_list[bw-1] += 1
  
h_max = max(h_b_list)
w_max = max(w_b_list)

h_cans = []
w_cans = []
for i in range(h):
  if h_b_list[i] == h_max:
    h_cans.append(i)
    
for i in range(w):
  if w_b_list[i] == w_max:
    w_cans.append(i)

for hi in h_cans:
  for wi in w_cans:
    if (hi+1, wi+1) not in targets:
      print(h_max+w_max)
      exit()
else:
  print(h_max+w_max-1)

