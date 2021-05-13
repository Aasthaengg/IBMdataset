n = int(input())
a = list(map(int,input().split()))

a.sort()
ans = [0,0]
temp_1 = 0
sign = 0

for i in range(1,n+1):
  temp = a[-i]

  if temp == temp_1:
    temp_1 = 0
    ans[sign] = temp
    if sign == 1:
      break
    sign = 1
  else:
    temp_1 = temp

print(ans[0]*ans[1])