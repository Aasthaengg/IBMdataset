n,k=(int(x) for x in input().split())

test_points=list(map(int,input().split()))

for i in range(k,n):
  if test_points[i]>test_points[i-k]:

    print("Yes")
  else:
    print("No")