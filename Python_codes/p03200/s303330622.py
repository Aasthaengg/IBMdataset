def integration(s):
  itg = [0]
  counter = 0
  for x in s:
    if x == "B":
      counter += 1
    itg.append(counter)
  return itg

def solve(itg, left, right):
  n = right-left
  if n <= 1:
    return 0
  mid = (left+right)//2
  a = solve(itg, left, mid)
  b = solve(itg, mid, right)
  res = a + b + (itg[mid]-itg[left])* \
    (right-mid-(itg[right]-itg[mid]))
  return res

s = input()
print(solve(integration(s), 0, len(s)))
