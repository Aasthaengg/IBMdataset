h,w=map(int,input().split())
a=['.'*(w+2)]+['.'+input()+'.' for _ in range(h)]+['.'*(w+2)]
for i in range(h):
  for j in range(w):
    if a[i][j]=='#':
      if not(a[i+1][j]=='#' or a[i-1][j]=='#' or a[i][j+1]=='#' or a[i][j-1]=='#'):
        print('No')
        exit()
print('Yes')
