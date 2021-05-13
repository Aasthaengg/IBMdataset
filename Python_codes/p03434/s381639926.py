n = int(input())
a = [int(an) for an in input().split()]
ans = a[0]
if n > 1:
  a.sort(reverse=True)
  ans = sum(a[::2]) - sum(a[1::2])
print(ans)