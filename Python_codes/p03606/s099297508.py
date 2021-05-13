a = []
for i in range(int(input())):
  l, r = map(int,input().split())
  a.append(r-l+1)
print(sum(a))