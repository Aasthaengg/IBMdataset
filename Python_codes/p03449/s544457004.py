n=(int)(input())
a = [list(map(int, input().split(" "))) for i in range(2)]
maxi = 0
for i in range(n):
  temp = sum(a[0][:i + 1]) + sum(a[1][i:])
  if maxi < temp:
    maxi = temp
print(maxi)