h, w, a, b = map(int, input().split())
for i in range(h):
  s = [0]*a+[1]*(w-a)
  t = [1]*a+[0]*(w-a)
  if i < b:
    print("".join(map(str, s)))
  else:
    print("".join(map(str, t)))