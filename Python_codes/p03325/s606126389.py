N = int(input())
a = list(map(int, input().split()))
ans = 0
for ai in a:
  while not ai % 2:
    ai //= 2
    ans += 1
    
print(ans)