O = str(input())
E = str(input())
E = E + " "
ans = ""
i = 0

while i<len(O):
  ans = ans + O[i] + E[i]
  i = i + 1

print(ans.rstrip(" "))