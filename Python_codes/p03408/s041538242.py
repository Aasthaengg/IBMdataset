N = int(input())
dic = {}
for i in range(N):
  a = input()
  dic[a] = dic.get(a, 0) + 1
M = int(input())
for i in range(M):
  b = input()
  dic[b] = dic.get(b, 0) - 1
d = sorted(dic.values(), reverse = True)
print(max(0, d[0]))