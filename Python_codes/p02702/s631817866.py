S = str(input())
li = [0] * 2019
ans = 0
li[0] = 1

d = 1
s = 0
for i in S[::-1]:
  s += int(i) * d
  s = s % 2019
  li[s] += 1
  d *= 10
  d = d % 2019
  
for l in li:
  ans += l * (l-1) // 2

print(ans)