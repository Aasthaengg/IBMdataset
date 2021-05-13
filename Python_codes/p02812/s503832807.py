N = int(input())
S = input()
if not "ABC" in S:
  print(0)
  exit()
else:
  ans = S.count("ABC")
print(ans)