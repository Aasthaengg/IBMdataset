A = list(input())
backet = [0] * (ord('z') - ord('a') + 1)

for a in A:
  backet[ord(a) - ord('a')] += 1
n = len(A)
ans = n*(n-1)//2 + 1
for b in backet:
  ans -= b*(b-1)//2
print(ans)
