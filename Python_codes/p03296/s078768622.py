N = int(input())
As = list(map(int, input().split()))
r = 0
cA = -1
cl = 0
As.append(-1)
for A in As:
  if A != cA:
    r += cl//2
    cA = A
    cl = 1
  else:
    cl += 1
print(r)
