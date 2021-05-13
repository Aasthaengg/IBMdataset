n = int(input())
a_list = list(map(int,input().split()))
c = 0
for a in a_list:
  for i in range(1,31):
    if a%(2**i) == 0:
      c += 1
    else:
      break
print(c)