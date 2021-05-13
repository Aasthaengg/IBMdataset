s = list(input())
ans = []
for i in range(len(s) - 2):
  num = s[i] + s[i + 1] + s[i + 2]
  ans.append(abs(753 - int("".join(num))))
print(min(ans))