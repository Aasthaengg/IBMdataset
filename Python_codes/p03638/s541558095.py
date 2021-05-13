H, W = map(int, input().split())
n = int(input())
a = map(int, input().split())

alist = []
i = 1
for ai in a:
  alist.extend([str(i)]*ai)
  i += 1

i = 0
for h in range(H):
  start = h * W
  end = start + W
  if h % 2 == 0:
    print(' '.join(alist[start:end]))
  else:
    print(' '.join(alist[end-1:start-1:-1]))

  
