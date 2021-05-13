n = int(input())
ll = list(map(int, input().split()))
ans = 3**n
odd = 1
for l in ll:
  if l % 2 == 1:
    pass
  elif l % 2 == 0:
    odd *= 2

print(ans - odd)