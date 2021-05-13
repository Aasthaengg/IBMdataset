def dev(n):
    return int(n / 2)

N = int(input())
li = list(map(int, input().split()))
flag = True
an = 0
while True:
 for i in range(N):
    if li[i] % 2 != 0:
      flag = False
 if flag:
  li = list(map(dev, li))
  an += 1
 else:
     break
print(an)