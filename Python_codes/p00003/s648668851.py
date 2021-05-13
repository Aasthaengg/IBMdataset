for _ in range(int(input())):
  a, b, c = sorted(map(int, input().split()))
  if a * a + b*b == c* c:
    print("YES")
  else:
    print("NO")