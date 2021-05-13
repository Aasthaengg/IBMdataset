a, b = map(int, input().split())
s = list(input())
s[b-1] = s[b-1].lower()

t = ""
for i in range(a):
  t += s[i]
  
print(t)