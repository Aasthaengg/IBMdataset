city={1:0,2:0,3:0,4:0}
for q in range(3):
    n,k=map(int,input().split())
    city[n]+=1
    city[k]+=1


if min(city.values()) ==0 or max(city.values())==3:
    print("NO")
else:
    print("YES")