x, t = input().split()
a, b = map(int, input().split())
u = input()
dic = {x:a, t:b}

for i in dic.keys():
  if i == u:
    dic[i] -= 1

print(dic[x], dic[t])