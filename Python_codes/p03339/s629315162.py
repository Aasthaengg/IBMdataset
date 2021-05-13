n = int(input())
S = list(input())
left = []
right = []
l = 0
r = 0
wa = []
for i in range(n):
  if i == 0:
    l += 0
    r += 0
    left.append(l)
    right.append(r)
  else:
    if S[i-1] == "W":
      l += 1
    left.append(l)
    if S[n-i] == "E":
      r += 1
    right.append(r)
for j in range(n):
  wa.append(left[j] + right[n-1-j])
print(min(wa))
