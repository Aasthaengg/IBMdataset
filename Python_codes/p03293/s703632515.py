def rotate(l, n):
    return l[-n:] + l[:-n]

s = input()
t = input()

flg = False
for i in range(len(s)):
  flg = flg or rotate(s, i) == t

print("Yes" if flg else "No")