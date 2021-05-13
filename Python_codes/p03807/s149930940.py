n = int(input())
a = list(map(int, input().split()))
even = 0
not_even = 0
for v in a:
  if v%2==0: even += 1
  else: not_even += 1
  if not_even == 2:
    even += 1
    not_even = 0
print("YES" if not_even == 0 else "NO")