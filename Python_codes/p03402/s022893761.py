a,b=map(int,input().split())
ans1=['.']*2500
ans2=['#']*2500
for i in range(b-1):
  ans1[2*i]='#'
for i in range(a-1):
  ans2[2*i]='.'
print(100,100)
for i in range(25):
  print(''.join(ans1[100*i:100*i+100]))
  print('.'*100)
for i in range(25):
  print('#'*100)
  print(''.join(ans2[100*i:100*i+100]))
