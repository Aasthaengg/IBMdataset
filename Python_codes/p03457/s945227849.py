N = int(input())
states = []
for n in range(N):
  t, x, y = map(int, input().split())
  states.append((t, x, y))

current = (0, 0, 0)
for next_ in states:
  diff_time = next_[0] - current[0]
  diff_dist = abs(next_[1] - current[1]) + abs(next_[2] - current[2])
  if diff_dist > diff_time:
    print("No")
    break
  elif diff_time % 2 == diff_dist % 2:
    current = next_
  else:
    print("No")
    break

if current == states[-1]:
	print("Yes")