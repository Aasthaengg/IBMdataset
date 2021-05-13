from random import randint
n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range (len(l)-1) :
  try:
    if l[i] == l[i + 1]:
        ans += 1
        l[i + 1] = randint(0, 10000)
  except:
    continue
print(ans)