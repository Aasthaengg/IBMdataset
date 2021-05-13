n = int(input())
odd = []
even = []
for i in range(1, n+1):
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)
print(len(odd)/n)