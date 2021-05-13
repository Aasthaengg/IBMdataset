N, x = map(int, input().split())
child_list = list(map(int, input().split()))

count = 0
for i, child in enumerate(sorted(child_list)):
  x -= child
  if x < 0:
    break
  if (i == len(child_list) - 1) and x != 0:
    break
  count += 1

print(count)