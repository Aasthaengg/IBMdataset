S = input()
correct = "CODEFESTIVAL2016"
cnt = 0
for s, c in zip(S, correct):
  if(s != c):
    cnt += 1
print(cnt)