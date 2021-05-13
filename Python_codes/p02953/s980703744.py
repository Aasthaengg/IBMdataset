n=int(input())
l=list(map(int,input().split()))
con=l[0]-1

for i in range(n-1):
  con=max(con,l[i])
  if l[i]-l[i+1]>1:
    print("No")
    exit()
  if l[i]>l[i+1] and l[i+1]<con-1:
    print("No")
    exit()
print("Yes")