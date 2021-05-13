n = int(input())

strlist = [input() for i in range(n)]
intlist = [int(x) for x in strlist]
sortlist = sorted(intlist)

temp = 0
ans = 0

for d in sortlist:
  if int(d) > temp:
    temp = int(d)
    ans += 1

print(ans)