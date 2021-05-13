n,m=map(int,input().split())
a=list(map(int,input().split()))
a_sort=[]
a_sort=sorted(a,reverse=True)
sum=0
for i in a:
  sum+=i
b_sort=a_sort[0:m]
for j in b_sort:
 if j<sum/(4*m):
    print("No")
    exit()
print("Yes")