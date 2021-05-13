n = int(input())
l = list(map(int,input().split()))

l.append(0)
_n = int(len(l)/2)

a = 0
b = 0

l.sort(reverse=True)

for i in range(_n):
  a += l[i*2]
  b += l[i*2 + 1]

print(a-b)