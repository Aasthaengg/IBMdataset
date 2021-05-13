h,w=map(int, input().split())
w1=['.'*(w+2)]
s=w1+['.'+input()+'.' for _ in range(h)]+w1

for i in range(1,h+1):
  for j in range(1,w+1):
    if s[i][j]=='.':
      t=s[i-1][j-1:j+2]+s[i][j-1:j+2]+s[i+1][j-1:j+2]
      s[i]=s[i][:j]+str(t.count('#'))+s[i][j+1:]
  print(s[i][1:-1])