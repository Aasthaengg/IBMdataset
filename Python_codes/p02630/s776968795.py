n = int(input())

a = list(map(int, input().split()))
defo = sum(a)
default = [0]*100001
for i in a:
  default[i]+=1

q = int(input())
for _ in range(q):
  b, c = map(int, input().split())
  defo = defo + (c-b)*default[b]
  print(defo)
  default[c] += default[b]
  default[b] = 0