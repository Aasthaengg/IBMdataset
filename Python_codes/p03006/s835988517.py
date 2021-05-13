#https://atcoder.jp/contests/diverta2019-2/submissions/11229318
n = int(input())
t = [tuple(map(int, input().split())) for _ in range(n)]
s = set(t)
cnt = 0
for i in range(n-1):
  for j in range(i+1,n):
    u,v = t[i]
    x,y = t[j]
    p = u-x; q = v-y
    c = sum((x-p, y-q) in s for x,y in t)
    if cnt < c: cnt = c
print(n-cnt)
