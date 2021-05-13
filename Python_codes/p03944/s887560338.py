w, h, n = map(int, input().split())
st = set()
for i in range(n):
  x, y, a = map(int, input().split())
  if a == 1:
    for k in range(x):
      for l in range(h):
        st.add((k, l))
  elif a == 2:
    for k in range(x, w):
      for l in range(h):
        st.add((k, l))
  elif a == 3:
    for k in range(w):
      for l in range(y):
        st.add((k, l))
  elif a == 4:
    for k in range(w):
      for l in range(y, h):
        st.add((k, l))
print(w * h - len(st))