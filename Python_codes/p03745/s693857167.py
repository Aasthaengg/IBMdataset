n = int(input())
a = list(map(int, input().split()))

before = a[0]
ok = "" #増加ならTrue
cnt = 0
for i in range(1,n):
  if ok == "":
    if before < a[i]:
      ok = True
    elif before > a[i]:
      ok = False
  elif ok:
    if before > a[i]:
      cnt += 1
      ok = ""
  elif not ok:
    if before < a[i]:
      cnt += 1
      ok = ""
  before = a[i]
print(cnt+1)