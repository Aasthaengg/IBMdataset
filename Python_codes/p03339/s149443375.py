n = int(input())
s = input()
countw = 0
counte = 0
ans = [0]*n
for i in range(1, n):
  if s[i-1] == "W":
    countw += 1
  if i != n:
    ans[i] += countw
  if s[-i] == "E":
    counte += 1
  ans[n-i-1] += counte

print(min(ans))