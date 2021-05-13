a,b,k=map(int,input().split())
l_left = list(range(a, min(a+k, b+1)))
l_right = list(range(b, max(b-k, a-1), -1))
s = sorted(list(set(l_left+l_right)))
for e in s:
  print(e)