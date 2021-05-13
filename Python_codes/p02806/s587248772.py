n = int(input())
s = [[] for i in range(n)]
#print(s)
for i in range(n):
  s[i] = list(input().split())
kyokumei = input()
ans = 0
for i in range(n):
  if s[i][0] == kyokumei:
    for j in range(i+1,n):
      ans += int(s[j][1])
    break
print(ans)