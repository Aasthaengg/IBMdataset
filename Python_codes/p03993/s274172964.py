n = int(input())
a = list(map(int,input().split()))
ans = 0
for index,aa in enumerate(a):
  if index+1 == a[aa-1]:
    ans += 1
print(int(ans/2))