a, b, k = map(int, input().split())

min = a
if b < min:
  min = b

ans_lists = []
for i in range(1, min+1, 1):
  if a%i == 0 and b%i == 0:
    ans_lists.append(i)

ans_lists.reverse()
ans = ans_lists[k-1]

print(ans)