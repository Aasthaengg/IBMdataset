n = int(input())
x = list(map(int, input().split()))
h = list(map(int, input().split()))

t = x[0]
a = x[1]
cnt = 1000000000000000000000
ans = 0
for i in range(n):
  tmp = abs(t-(h[i]*0.006)-a)
  if cnt > tmp:
    cnt = tmp
    ans = i+1
print(ans)
