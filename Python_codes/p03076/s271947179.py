l = [int(input()) for _ in range(5)]

ans = 0
min_div = 10
for i in l:
  ans += 10 * ((i + 10 - 1) //10)
  if i % 10 != 0:
  	min_div = min(min_div, i % 10)
print(ans - (10 - min_div))
