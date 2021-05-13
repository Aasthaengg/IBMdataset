n=int(input())
x=list(map(int,input().split()))
sorted_x=sorted(x)
min_m,max_m=sorted_x[n//2-1],sorted_x[n//2]

for i in range(n):
  if x[i]<=min_m:
    print(max_m)
  else:
    print(min_m)
    
