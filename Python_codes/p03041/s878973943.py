n,k = map(int,input().split())
s = input()
ss = s.lower()
ans = ""
for i in range(n):
  ans += ss[i] if i == k-1 else s[i]


print(ans)