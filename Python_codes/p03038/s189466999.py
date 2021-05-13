n, m = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(m)]

A.sort()
BC.sort(key=lambda k: -k[1])

stack = []
cnt = 0
for b, c in BC:
  for _ in range(b):
    stack.append(c)
    cnt += 1
    if cnt > n:
      break

for i in range(min(n, len(stack))):
  if A[i] < stack[i]:
    A[i] = stack[i]
  else:
    break
    
print(sum(A))