a = list(input())
b = list(input())

ans = ""
for i in range(1, len(a) + len(b) + 1):
  if i % 2 == 1:
    ans += a[i // 2]
  else:
    ans += b[i // 2 - 1]
    
print(ans)