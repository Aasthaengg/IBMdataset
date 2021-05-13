a,b = list(map(int,input().split()))

ans = -1

for i in range(1,10100):
  if i // 12.5== a and i // 10 == b:
    ans = i
    break

print(ans)