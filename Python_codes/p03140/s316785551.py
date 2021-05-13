n = int(input())
s1 = input()
s2 = input()
s3 = input()

ans = 0
for i in range(n):
  if s1[i] == s2[i] and s2[i] == s3[i]:
    pass
  elif s1[i] == s2[i] or s1[i] == s3[i] or s2[i] == s3[i]:
    ans += 1
  else:
    ans += 2
print(ans)