#coding:utf-8
n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

p1 = 0
p2 = 0
p3 = 0

for i in p:
  if i <= a:
    p1 += 1
  elif i >= (a+1) and i <= b:
    p2 += 1
  elif i >= (b+1):
    p3 += 1

print(min(min(p1, p2), p3))
