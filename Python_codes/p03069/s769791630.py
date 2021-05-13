n = int(input())
s = input()

key = [0]*(n+1)
for i in range(n):
  key[i+1] = key[i]
  if s[i] == "#":
    key[i+1] += 1

ans = n+1
for i in range(n+1):
  sub = 2*key[i]+n-i-key[-1]
  if ans > sub:
    ans = sub

print(ans)