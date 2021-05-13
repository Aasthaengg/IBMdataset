n = int(input())
B = list(map(int, input().split()))
ret = []
enabled = True

def get_latest():
  for i in range(len(B)):
    if len(B) - i == B[len(B) - i - 1]:
      break
  else:
    global enabled
    enabled = False
  ret.append(B.pop(len(B) - i - 1))
  if B:
    get_latest()

get_latest()
if enabled:
  for i in range(n):
    print(ret[n - i - 1])
else:
  print(-1)