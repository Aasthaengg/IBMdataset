n = int(input())
s = list(input())

ans = [None] * (n-1)

for i in range(1,n):
  a = s[0:i]
  b = s[i:n]

  ans[i-1] = len(set(b))-len((set(b)-set(a)))

ans.sort(reverse = True)

print(ans[0])
