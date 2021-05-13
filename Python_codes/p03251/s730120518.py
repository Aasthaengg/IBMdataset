N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

for i in range(-100,100):
  if X<i<=Y and max(x)<i and min(y)>=i:
    print("No War")
    exit()

print("War")