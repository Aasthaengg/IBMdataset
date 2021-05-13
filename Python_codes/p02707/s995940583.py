n = int(input())
a = [int(i) for i in input().split()]
dic = {}
for ni in range(n):
  dic[ni+1] = 0
for ai in a:
  dic[ai] += 1
for di in dic:
  print(dic[di])