S = input()

list_S = list(S)

list_T = list("CODEFESTIVAL2016")

ans = 0
for i in range(len(list_S)):
  if list_S[i] != list_T[i]:
    ans =ans +1

print(ans)