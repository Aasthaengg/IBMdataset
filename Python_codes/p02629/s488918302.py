N = int(input())
p = N
s = []
abt = "abcdefghijklmnopqrstuvwxyz"
ans = ""

while p > 0:
   p -= 1
   s.append(p % 26)
   p //= 26

for i in s[::-1]:
    ans += abt[i]

print(ans)
