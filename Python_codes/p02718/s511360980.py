n,m = map(int,input().split())
x = list(map(int,input().split()))
x.sort(reverse = True)
sumx = sum(x)
limit = sumx/4/m
#print(limit)
if x[m-1]>=limit:
    print("Yes")
else:
    print("No")