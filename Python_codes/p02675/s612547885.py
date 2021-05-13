n = input()
n = int(n[-1])

if n in [2, 4, 5, 7, 9]:
  ans = 'hon'
elif n in [0, 1, 6, 8]:
  ans = 'pon'
else:
  ans = 'bon'
print(ans)
