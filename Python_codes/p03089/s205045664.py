N = int(input())
B = list(map(int, input().split()))

def solve(arr):
  ret = []
  while len(arr) > 0:
    before = len(arr)
    for i in reversed(range(len(arr))):
      if arr[i] == i + 1:
        ret.append(arr.pop(i))
        break
    if len(arr) == before:
      return None
  return list(reversed(ret))

A = solve(B)
#print(A)

if A == None:
  print(-1)
else:
  for a in A:
    print(a)