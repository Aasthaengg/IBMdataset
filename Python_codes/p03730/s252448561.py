a, b, c = map(int, input().split())
for y in range(1,101):
  if ((b * y + c) / a).is_integer():
    print("YES")
    exit(0)
print("NO")