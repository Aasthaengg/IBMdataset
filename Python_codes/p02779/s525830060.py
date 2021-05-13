n = int(input())
a = list(map(int, input().split()))
d = set()
for x in a:
  if x in d:
    print("NO")
    quit()
  d.add(x)
print("YES")
