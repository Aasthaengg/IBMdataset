n = int(input())
a = list(map(int,input().split()))
mid = sum(a) / len(a)
b = float('inf')
for i, j in enumerate(a):
  sa = abs(mid - j)
  if(sa < b):
    b = sa
    ans = i
print(ans)
