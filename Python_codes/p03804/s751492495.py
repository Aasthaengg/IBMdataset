n, m = map(int,input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n - m + 1):
  for j in range(n - m + 1):
    for k in range(m):
      #print(a[i+k][j:j+m], b[k])
      if a[i+k][j:j+m] != b[k]:
        break
    else:
      print('Yes')
      exit()
print('No')
