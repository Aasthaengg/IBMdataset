n = int(input())
a = input()
b = input()
c = input()
ans = 0
for i in range(n):
  a_ = a[i]
  b_ = b[i]
  c_ = c[i]
  if a_ == b_ and b_ != c_:
    ans += 1
  elif a_ == c_ and b_ != c_:
    ans += 1
  elif b_ == c_ and a_ != c_:
    ans += 1
  elif a_==b_ and a_==c_:
    ans += 0
  else:
    ans += 2
print(ans)