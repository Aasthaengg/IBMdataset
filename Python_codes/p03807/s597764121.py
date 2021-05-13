n=int(input())
i = list(map(int, input().split()))
s=0
for j in range(n):
  if i[j]%2==1:
    s+=1
if s%2==0:
  print("YES")
else:
  print("NO")