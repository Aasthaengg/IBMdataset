n = int(input())
title = []
sec = []
for i in range(n):
  s, t = input().split()
  title.append(s)
  sec.append(int(t))
x = input()
print(sum(sec[title.index(x) + 1:]))