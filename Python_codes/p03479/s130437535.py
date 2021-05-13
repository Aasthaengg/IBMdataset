X, Y = list(map(int, input().split()))

ans = []
num = X
while(num <= Y):
  ans.append(num)
  num *= 2

print(len(ans))
