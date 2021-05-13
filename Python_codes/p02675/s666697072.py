n = int(input())
ans = 'hon'
if n % 10 in [0, 1, 6, 8]:
  ans = 'pon'
elif n % 10 == 3:
  ans = 'bon'
print(ans)