H,W=map(int,input().split())
n=['#']*(W+2)
print(''.join(n))
for i in range(H):
  h=input()
  lh=['#',h,'#']
  print(''.join(lh))
print(''.join(n))
