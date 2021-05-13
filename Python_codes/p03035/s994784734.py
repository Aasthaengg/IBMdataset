A, B = map(int, input().split())

if 6 <= A <= 12:
  B = B / 2
elif 5 >= A:
  B = 0
else:
  pass

print(int(B))