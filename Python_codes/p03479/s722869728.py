x,y = map(int,input().split())

tmp = x
ans = []
while True:
  if(tmp > y):
    break
  else:
    ans.append(tmp)
    tmp = 2*tmp
    
print(len(ans))