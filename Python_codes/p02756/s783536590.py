s = input()
q = int(input())
r = 0
S = ['','']
for _ in range(q):
  d = input().split()
  if d[0]=='1':
    r ^= 1
  else:
    S[(int(d[1])+r)%2] += d[2]
s = S[1][::-1] + s + S[0]
if r:
  s = s[::-1]
print(s)