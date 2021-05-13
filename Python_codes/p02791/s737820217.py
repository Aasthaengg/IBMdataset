n = int(input())
p = map(int, input().split())

min_p = 2 * 10**5 + 1
ans = list()
for i, v in enumerate(p, 1):
  if min_p > v:
    min_p = v
    ans.append(v)

print(len(ans))


