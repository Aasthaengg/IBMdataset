n = int(input())
a = list(map(int, input().split()))
ans = 0
i = 0
while i < n:
  if i+1 == a[i]:
    ans += 1
    i += 1
  i += 1
    
print(ans)