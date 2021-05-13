A = [1, 3, 5, 7, 8, 10, 12]
B = [4, 6, 9, 11]
C = [2]

x, y = map(int, input().split())
ans = "No"
for group in [A, B, C]:
  if x in group and y in group:
    ans = "Yes"
print(ans)
