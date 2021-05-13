import sys
read = sys.stdin.read
a = list(map(int,read().split()))
if len(set(a)) == 4:
  if max([a.count(x) for x in range(1,5)]) == 2:
    print("YES")
    exit()
print("NO")