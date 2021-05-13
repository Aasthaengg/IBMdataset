n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
s.sort(key=lambda x:(x[1],x[1]-x[0]))
time = 0
ans = 1
for v in s:
  time += v[0]
  if time > v[1]:
    ans = 0
print('Yes' if ans else 'No')