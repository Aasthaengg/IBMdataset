N = int(input())
S = input()
ans = S.count("E")
a = ans
for i in range(N):
  if S[i] == "E":
    a -= 1
    ans = min(ans, a)
  else:
    a += 1
print(ans)