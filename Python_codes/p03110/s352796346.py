n = int(input())
a = [list(input().split()) for nesya in range(n)]
c = 0
for hoge in a:
  if hoge[1] == 'JPY':
    c += int(hoge[0])
  else:
    c += float(hoge[0])*380000
print(c)