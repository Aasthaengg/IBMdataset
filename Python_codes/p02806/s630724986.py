n = int(input())
st = []
for i in range(n):
  s, t = input().split()
  st.append((s, int(t)))
x = input()

ans, f = 0, 0
for s, t in st:
  if f:
    ans += t
  if s == x:
    f = 1
print(ans)