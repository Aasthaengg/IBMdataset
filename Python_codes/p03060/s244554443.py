N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

ans = 0
for x,y in zip(X,Y):
  if x-y >0:
    ans += x-y
print(ans)