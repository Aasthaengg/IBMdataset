s = input()
N = len(s)
g = s.count('g')
p = s.count('p')
ans = g-p
if N%2==1:
  ans -= 1
ans //= 2
print(ans)
