n = int(input())

mod = 10**9 + 7

dict = dict()
list = []
res = 1
for i in range(n):
  x = input()
  list.append(x)
  if x in dict and list[i - 1] != x:
    res += dict[x]
    dict[x] = res
  elif x not in dict:
    dict[x] = res

print(res % mod)