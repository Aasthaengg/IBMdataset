S=input()
K=int(input())
for i in range(len(S)):
  if i==K-1:
    print(S[i])
    exit()
  if S[i]!="1":
    print(S[i])
    exit()
print(1)