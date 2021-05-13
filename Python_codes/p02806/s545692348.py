n = int(input())
title = []
p_time = []
for i in range(n):
  buf = input().split()
  title.append(buf[0])
  p_time.append(int(buf[1]))
s_title = input()
for i in range(n):
  p_time.pop(0)
  if title[i] == s_title:
    break
print(sum(p_time))