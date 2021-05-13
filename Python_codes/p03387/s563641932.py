A,B,C=map(int,input().split())
odd = A%2+B%2+C%2
answer = 0
if odd == 1:
  answer = 1
  if not A%2:
    A += 1
  if not B%2:
    B += 1
  if not C%2:
    C += 1
elif odd == 2:
  answer = 1
  if A%2:
    A += 1
  if B%2:
    B += 1
  if C%2:
    C += 1
D = sorted([A,B,C])
answer += (D[2]-D[0])//2+(D[2]-D[1])//2
print(answer)