n = int(input())
l = list(map(int, input().split()))

m = max(l)
o = sum(l) - m

if m < o:
  print('Yes')
else:
  print('No')