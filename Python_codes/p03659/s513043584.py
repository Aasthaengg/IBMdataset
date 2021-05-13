n = int(input())
a_lst = list(map(int, input().split()))

x = a_lst[0]
y = sum(a_lst[1:])
diff = abs(y - x)
for a in a_lst[1:-1]:
  x += a
  y -= a
  diff = min(diff, abs(y - x))
print(diff)