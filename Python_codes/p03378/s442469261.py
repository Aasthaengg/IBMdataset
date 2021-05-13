N,M,X = map(int,input().split())
l = list(map(int,input().split()))
num = X
ans1 = 0
ans2 = 0
while num <= N:
  if num in l:
    ans1 += 1
  num += 1
num = X
while num >= 0:
  if num in l:
    ans2 += 1
  num -= 1
print(min(ans1,ans2))