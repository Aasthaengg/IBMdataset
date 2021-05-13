a,b,c = list(map(int,input().strip().split()))
for i in range(1,b):
  if a * i % b == c:
    print("YES")
    exit()
print("NO")