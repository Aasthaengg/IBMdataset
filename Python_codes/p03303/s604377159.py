S = input()
w = int(input())
for i in range(len(S)):
  if i % w == 0: print(S[i],end = "")