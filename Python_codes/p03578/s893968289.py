import collections
n = int(input())
d = [int(i) for i in input().split()]
m = int(input())
t = [int(i) for i in input().split()]

c = collections.Counter(d)


for i in t:
  if i in c:
    c[i] = c[i] - 1
  elif i not in c:
    print("NO")
    exit()


for i in c:
  if c[i] < 0:
    print("NO")
    exit()

print("YES")