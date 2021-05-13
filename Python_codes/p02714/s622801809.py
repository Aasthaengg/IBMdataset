from collections import Counter
n = int(input())
s = list(input())
c = Counter(s)
ans = c["R"]*c["G"]*c["B"]
for i in range(n-2):
  for j in range(1,n):
    if i+2*j >= n:
      break
    if sorted([s[i],s[i+j],s[i+2*j]]) == ["B","G","R"]:
      ans -= 1
print(ans)