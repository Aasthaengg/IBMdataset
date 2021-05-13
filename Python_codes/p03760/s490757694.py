O = input()
E = input()

ans = ""
for i in range(len(O) - 1):
  ans += O[i] + E[i]

ans += O[-1]
if len(O) - len(E) == 0:
  ans += E[-1]

print(ans)
