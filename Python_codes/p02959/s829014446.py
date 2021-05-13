n = int(input())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))
ans = 0
car = 0
for i in range(n):
  plus = min(blst[i] + car, alst[i])
  ans += plus
  if plus == alst[i]:
    car = blst[i] + car - alst[i]
    car = min(car, blst[i])
  else:
    car = 0
ans += min(car, alst[-1])
print(ans)