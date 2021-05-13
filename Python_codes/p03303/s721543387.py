s = input()
w = int(input())
a = ""
for i,j in enumerate(s):
  if i % w == 0:
    a += j
print(a)