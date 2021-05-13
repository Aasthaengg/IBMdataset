n = int(input())
a = [int(i) for i in input().split()]
ans = 'APPROVED'
for ai in a:
  if ai % 2 == 0 and ai % 3 != 0 and ai % 5 != 0:
    ans = "DENIED"
print(ans)