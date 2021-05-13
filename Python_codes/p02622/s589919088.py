S=input()
T=input()

stringlen = len(S)
cnt = 0

for i in range(stringlen):
  if S[i] != T[i]:
    cnt=cnt+1

print(cnt)