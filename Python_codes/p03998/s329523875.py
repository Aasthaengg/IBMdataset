D = {}
D["a"] = list(input())[::-1]
D["b"] = list(input())[::-1]
D["c"] = list(input())[::-1]
p = "a"

while D[p]:
  p = D[p].pop()

print(p.upper())