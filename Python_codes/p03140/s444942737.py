N,A,B,C = int(input()), input(), input(), input()
ans = 0
for a,b,c in zip(A,B,C):
  if a == b and b ==c: continue
  elif a==b or b==c or c==a: ans += 1
  elif a != b and b != c and c != a: ans += 2
print(ans)