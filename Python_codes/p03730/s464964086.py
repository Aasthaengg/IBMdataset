a,b,c= map(int,input().split())
for i in range(b):
  if (a*i-c)%b ==0:
    print("YES")
    exit()
print("NO")