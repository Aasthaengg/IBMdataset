n = int(input())
s = list(input().split())

num = 0
l = []

for i in s:
  if i not in l:
    num += 1
  l.append(i)
if num == 3:
    print('Three')
else:
    print('Four')