N = int(input())
s = [None] * N
t = [None] * N
for i in range(N):
  p, q = input().split()
  s[i] = p
  t[i] = int(q)
X = input()
print(sum(t[s.index(X)+1:]))