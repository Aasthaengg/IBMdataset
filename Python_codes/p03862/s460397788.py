_n, x = map(int, input().split())
boxes = list(map(int, input().split()))
cnt = 0
for idx, _b  in enumerate(boxes):
  if idx == 0:
    continue
  else:
    if boxes[idx] + boxes[idx - 1] >= x:
      sum = boxes[idx] + boxes[idx - 1]
      if boxes[idx] - (sum - x) >= 0:
        boxes[idx] -= sum - x
      else:
        boxes[idx] = 0
      cnt += sum - x
    else:
      continue

print(cnt)