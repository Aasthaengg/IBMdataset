h,w = map(int, input().split())

A = [input() for i in range(h)]

print("#" * (w+2))
for i in range(h):
  s = ""
  s = "#" + A[i] + "#"
  print(s)

print("#" * (w+2))