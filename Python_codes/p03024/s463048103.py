S = str(input())
count_y = 0
count_n = 0
for i in range(len(S)):
  if S[i] == "o":
    count_y += 1
  else:
    count_n += 1
  if count_n>7:
    print("NO")
    exit()
print("YES")