s = input()
k = int(input())
ans = []
for i in range(len(s)):
  for j in range(i+1, len(s)+1):
    if j-i > k:break
    ans.append(s[i:j])
ans = sorted(list(set(ans)))
print(ans[k-1])