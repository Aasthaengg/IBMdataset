s = input()

ans = []

for n in range(0,len(s),2):
  ans.append(s[n])
print("".join(ans))