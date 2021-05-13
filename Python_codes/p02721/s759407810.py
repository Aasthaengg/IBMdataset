n, k, c = map(int, input().split())
s = input()
# record positions of included work days for leftmost and rightmost solutions
leftmost_solution = list()
rightmost_solution = list()
timer = -1
for idx in range(n):
  if s[idx] == "o" and timer <= 0:
    leftmost_solution.append(idx)
    if len(leftmost_solution) == k:
      break
    timer = c+1
  timer -= 1
timer = -1
for idx in range(n-1, -1, -1):
  if s[idx] == "o" and timer <= 0:
    rightmost_solution.append(idx)
    if len(rightmost_solution) == k:
      break
    timer = c+1
  timer -= 1
rightmost_solution.reverse()
for left, right in zip(leftmost_solution, rightmost_solution):
  if left == right:
    print(left+1)