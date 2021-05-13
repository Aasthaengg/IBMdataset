N = int(input())
L = list(map(int, input().split()))
l = []
for i in L:
  l.append(format(i, 'b')[::-1].find('1'))
print(min(l))