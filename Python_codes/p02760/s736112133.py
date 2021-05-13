a_1 = list(map(int,input().split()))
a_2 = list(map(int,input().split()))
a_3 = list(map(int,input().split()))
a = [a_1,a_2,a_3]
n = int(input())
for i in range(n):
  h = int(input())
  for j in range(3):
    for k in range(3):
      if(a[j][k]==h):
        a[j][k]=0
ans = "No"
for i in range(3):
  if(a[i][0]==0)and(a[i][0]==a[i][1])and(a[i][1]==a[i][2]):
    ans = "Yes"
for i in range(3):
  if(a[0][i]==0)and(a[0][i]==a[1][i])and(a[1][i]==a[2][i]):
    ans= "Yes"
if((a[0][0]==0)and(a[1][1]==a[2][2])and(a[0][0]==a[1][1]))or((a[0][2]==0)and(a[1][1]==a[2][0])and(a[0][2]==a[1][1])):
  ans = "Yes"
  
print(ans)
    
    
