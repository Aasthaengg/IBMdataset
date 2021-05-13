n = int(input())
s = input()
q = [chr(i) for i in range(65,65+26)]
ans = []
for i in s:
  al = q.index(i)
  al += n
  if al >= 26:
    al -= 26
  print(q[al],end='')