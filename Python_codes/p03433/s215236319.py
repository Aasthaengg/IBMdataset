N=int(input())
A=int(input())
flag=True
ans="No"

for i in range(0,A+1):
  if flag:
    for j in range(0,N//500+1):
      if i+500*j==N:
        ans="Yes"
        flag=False
        break

print(ans)