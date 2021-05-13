import copy

input()
ary = list(map(int, input().split()))
copy = copy.copy(ary)
ary.sort()
ans = 0

for a, c in zip(ary, copy):
  if a != c:
    ans += 1

print('YES' if ans <= 2 else 'NO')