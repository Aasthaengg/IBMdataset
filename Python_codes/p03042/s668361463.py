s = int(input())
s1 = s // 100
s2 = s % 100
c = 0
l = ["NA","YYMM","MMYY","AMBIGUOUS"]
if 1<=s2<=12:
  c += 1
if 1<=s1<=12:
  c += 2
print(l[c])