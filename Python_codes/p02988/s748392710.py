n = int(input())
p = list(map(int, input().split()))
def check(a, b, c):
  l = [a, b, c]
  l.sort()
  if l[1] == b:
    return True
  else:
    return False
cnt = 0
for i in range(n-2):
  if check(p[i], p[i+1], p[i+2]):
    cnt += 1
print(cnt)