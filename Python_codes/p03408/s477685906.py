n = int(input())
dic1 = {}
for i in range(n):
  temp = input()
  dic1.setdefault(temp, 0)
  dic1[temp] += 1
m = int(input())
for i in range(m):
  temp = input()
  dic1.setdefault(temp, 0)
  dic1[temp] -= 1
print(max(0, max(list(dic1.values()))))