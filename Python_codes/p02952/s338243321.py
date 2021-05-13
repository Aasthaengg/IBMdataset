N = int(input())
ichi = 9
hyaku = 900
man = 90000
if N < 10:
  print(N)
elif 10 <= N < 100:
  print(ichi)
elif 100 <= N <= 999:
  ans = N - 99
  print(ichi+ans)
elif 1000 <= N <= 9999:
  print(ichi+hyaku)
elif 10000 <= N <= 99999:
  ans = N - 9999
  print(ichi+hyaku+ans)
else:
  print(90909)