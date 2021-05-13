n = int(input())
a = input()
b = input()
c = input()
ans = 0
if a == b == c:
  ans = 0
else:
  for i in range(n):
    l = [a[i], b[i], c[i]]
    ans += len(list(set(l))) - 1
print(ans)