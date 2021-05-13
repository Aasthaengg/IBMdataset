n = int(input())
s = input()
rgb = s.count("R") * s.count("G") * s.count("B")
for i in range(n-2):
  for j in range(i+1, n-1):
    d = j - i
    k = j + d
    if n <= k: break
    if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
      rgb -= 1
print(rgb)      
