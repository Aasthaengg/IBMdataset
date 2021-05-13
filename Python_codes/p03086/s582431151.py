s = str(input().split())
S = list(s)

ans = 0
alist = []

for i in range(len(s)):
  if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
    ans += 1
  else:
    alist.append(ans)
    ans = 0
    
print(max(alist))