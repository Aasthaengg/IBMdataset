n = int(input())
sl = list(input())

bl = [0]
wl = [0]
a = 0
b = 0
for s in sl:
   if s == "#":
      b += 1
   if s == ".":
      a += 1
   bl.append(a)
   wl.append(b)

ans = float("inf")
for i in range(n):
   tmp = wl[i+1] + bl[-1] - bl[i+1]
   ans = min(ans, tmp)

ans = min(wl[-1],ans)
ans = min(bl[-1],ans)
print(ans)