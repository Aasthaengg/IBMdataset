l = input()
charl = list(input().split())
ans = ''
for i in range(len(charl[0])):
  ans += charl[0][i] + charl[1][i]
print(ans)