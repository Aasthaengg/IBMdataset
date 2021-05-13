n = int(input())
s, t = input(), input()

ans = 1<<30
for i in range(len(s)+1) :
  st = s[0 : i] + t
  if len(st) >= n and st[ : n] == s and st[-n : ] == t :
    ans = min(ans, len(st))
print(ans)