from collections import defaultdict
h, w = map(int, input().split())
A = defaultdict(int)
for _ in range(h):
  for x in str(input()):
    A[x] += 1
#print(A)
for k in A.keys():
  A[k] %= 4
#print(A)
if h%2 == 0 and w%2 == 0:
  if sum(A.values()) == 0:
    ans = 'Yes'
  else:
    ans = 'No'
else:
  cnt2 = 0
  for k in A.keys():
    if A[k] >= 2:
      cnt2 += 2
      A[k] %= 2
  rest = sum(A.values())
  if h%2 == 1 and w%2 == 1:
    if cnt2 <= h + w - 2 and rest == 1:
      ans = 'Yes'
    else:
      ans = 'No'
  else:
    if h%2 == 0 and cnt2 <= h and rest == 0:
      ans = 'Yes'
    elif w%2 == 0 and cnt2 <= w and rest == 0:
      ans = 'Yes'
    else:
      ans = 'No'
print(ans)