c = list("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")
N = int(input())
str = input()
ans = ""
for i in range(len(str)):
  ans += c[c.index(str[i]) + N]
  
print(ans)
