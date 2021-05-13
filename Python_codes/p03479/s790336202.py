X, Y = list(map(int, input().split()))

ans = 0
math = X
while(math <= Y):
  ans += 1
  math = math * 2

print(ans)