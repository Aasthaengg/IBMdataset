def solve():
  N, K, C = map(int, input().split())
  workable = [i for i, s in enumerate(input()) if s=="o"]
  if len(workable) == K:
    return workable
  
  def to_left():
    prev = workable[-1]+C+1
    for x in reversed(workable):
      if prev - x > C:
        yield x
        prev = x
  latest = set(to_left())
  if len(latest) > K:
    return []
  def to_right():
    prev = -C-1
    for x in workable:
      if x - prev > C:
        if x in latest:
          yield x
        prev = x
  return to_right()

for i in solve():
  print(i+1)
