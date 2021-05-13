A,B = map(int,input().split())
ans = 'Impossible'
ls =[A,B,A+B]
for i in ls:
  if i % 3 == 0:
    ans = 'Possible'
print(ans)