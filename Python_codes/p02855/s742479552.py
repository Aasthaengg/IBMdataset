H,W,K = list(map(int,input().split()))
MAP = [input() for i in range(H)]
CNT = [line.count("#") for line in MAP]
stack = 1
strcnt = 0
for idx, cnt in enumerate(CNT):
  sharp_cnt = 0
  if cnt == 0:
    stack += 1
  else:
    strcnt += 1
    line_lst = []
    for char in MAP[idx]:
      if char == "#":
        sharp_cnt += 1
        if sharp_cnt >= 2:        
          strcnt += 1
      line_lst += [str(strcnt)]
    for i in range(stack):
      print(" ".join(line_lst))
    stack = 1
else:
  if cnt == 0:
    for i in range(stack-1):
      print(" ".join(line_lst))
    stack = 1