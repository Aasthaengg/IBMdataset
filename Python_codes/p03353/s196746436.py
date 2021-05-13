s = input()
k = int(input())
moji = []
for i in range(len(s)):
  for j in range(1, k + 1):
    if j + i > len(s): break
    moji.append(s[i : i + j])
moji = list(set(moji))
moji.sort()
print(moji[k - 1])