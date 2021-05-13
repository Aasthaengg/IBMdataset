S = input()
s =[""]
i = 0
for j in range(1,len(S)+1):
  if S[i:j]!=s[-1] and S[i:j] != "":
    s.append(S[i:j])
    i=j
s.pop(0)
print(len(s))