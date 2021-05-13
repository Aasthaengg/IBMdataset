
a,b = map(int,input().split())
cnt = 0

cnt += max(a,b)
if a >= b:
  a -= 1
else:
  b -= 1

cnt += max(a,b)
print(cnt)