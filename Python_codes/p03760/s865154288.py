o = input()
e = input()
ans = ''
for i in range(len(e)):
  ans += o[i]+e[i]
print(ans if len(o)==len(e) else ans+o[-1])