A, B = map(int, input().split())
day = 0
for a in range(1, A):
  day += 1
if A <= B:
  day += 1
print(day)