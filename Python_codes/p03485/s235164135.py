a,b = list(map(int, input().split()))
avg=a+b
if avg%2==1:
  avg+=1
print(int(avg/2))