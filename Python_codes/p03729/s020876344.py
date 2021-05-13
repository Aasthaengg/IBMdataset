words = [s for s in input().split()]
if (words[0][-1]==words[1][0]) and (words[1][-1] == words[2][0]):
  print("YES")
else:
  print("NO")