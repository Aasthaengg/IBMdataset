n = int(input())
s1 = input()
s2 = input()

if s1[0] == s2[0]:
  result = 3
  last_pattern = "h"
  place = 1
else:
  result = 6
  last_pattern = "w"
  place = 2
while place < n:
  if last_pattern == "h":
    if s1[place] == s2[place]:
      result *= 2
      last_pattern = "h"
      place += 1
    else:
      result *= 2
      last_pattern = "w"
      place += 2
  else:
    if s1[place] == s2[place]:
      last_pattern = "h"
      place += 1
    else:
      result *= 3
      last_pattern = "w"
      place += 2
print(result % (7 + 10**9))