a,b,c = map(int, input().split())

t = 0
while t != b:
  t += 1
  if a*t%b == c:
    print("YES")
    exit()
print("NO")