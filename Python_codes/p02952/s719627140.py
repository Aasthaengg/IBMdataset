N = int(input())
if len(str(N)) == 1:
  ans = N
elif len(str(N)) == 2:
  ans = 9
elif len(str(N)) == 3:
  ans = N - 99 +9
elif len(str(N)) == 4:
  ans = 999 -99 + 9
elif len(str(N)) == 5:
  ans = N - 9999 + 999 - 99 +9
else:
  ans = 99999 - 9999 + 999 -99 +9
print(ans)