n, k = map(int, input().split())
s = input()
s = "_" + s + "_"

count = 0
for i in range(1, n+1):
  if s[i] == s[i-1] == "R" or s[i] == s[i+1] == "L":
    count += 1

print(min(n-1, count + k*2))