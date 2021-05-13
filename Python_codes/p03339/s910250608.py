n = int(input())
s = [p for p in input()]
w = [0]
e = [0]
mn = float("inf")
for i in range(n):
  if s[i] == 'W':
  	w.append(w[i]+1)
  else:
    w.append(w[i])
  e.append(i+1-w[i+1])
for i in range(n):
  if w[i]+e[n]-e[i+1] < mn:
    mn = w[i]+e[n]-e[i+1]
print(mn)